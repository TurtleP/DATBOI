from tkinter import *
from textbox import TextBox

#Define the frame
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(400, 256)) #Formatted as W * H
top.wm_title("DATBOI v0.5.0")
top["background"] = "#263238"

buttons = []

graphics = []
graphics.append(PhotoImage(file="assets/gears.png"))
graphics.append(PhotoImage(file="assets/wifi.png"))
graphics.append(PhotoImage(file="assets/about.png"))
graphics.append(PhotoImage(file="assets/debug.png"))

play_image = PhotoImage(file="assets/start.png")

canvas_items = list()

datBoi = PhotoImage(file="assets/datboi.png")

for i in range(len(graphics)):
	configButton = Button(top, border=0, highlightthickness=0)
	configButton["background"] = "#37474F"
	configButton["activebackground"] = "#37474F"
	configButton["highlightbackground"] = "#37474F"
	configButton["relief"] = "flat"
	configButton.config(image=graphics[i])
	configButton.place(x=0, y=i*32, width=32, height=32)
	canvas_items.append(list())
	buttons.append(configButton)

renderCanvas = Canvas(top, highlightthickness=0)
renderCanvas["background"] = "#263238"
renderCanvas.place(x=32, width=368, height=256)

currentTab = 0
def checkOpen(button):
	for i in range(len(graphics)):
		if i != button:
			buttons[i]["background"] = "#37474F"
			buttons[i]["activebackground"] = "#37474F"
			
			for j in range(len(canvas_items[i])):
				renderCanvas.itemconfig(canvas_items[i][j], state=HIDDEN)

		else:
			buttons[button]["background"] = "#263238"
			buttons[button]["activebackground"] = "#263238"

			for j in range(len(canvas_items[button])):
				renderCanvas.itemconfig(canvas_items[button][j], state=NORMAL)

			global currentTab 
			currentTab = button

def add_item(item):
	canvas_items[currentTab].append(item)

####
renderCanvas.create_image(270, 130, image=datBoi)

add_item(renderCanvas.create_text(30, 24, fill="#FFFFFF", text="Access Point Configuration", anchor="w", font=("assets/Roboto-Regular", 18, "normal")))
	
ssid_textbox = TextBox(renderCanvas, 112, 80, "SSID Name")
passwd_textbox = TextBox(renderCanvas, 112, 145, "Password", True)

for item in ssid_textbox.get_items():
	add_item(item)

for item in passwd_textbox.get_items():
	add_item(item)

start_button = Button(renderCanvas, border=0, highlightthickness=0)
start_button["background"] = "#263238"
start_button["activebackground"] = "#263238"
start_button.config(image=play_image)
start_button.place(x=172, y=210, width=32, height=32)

add_item(start_button)
###

def click(event):
	x, y = event.x, event.y
	print(currentTab)
	if currentTab == 0:
		if ssid_textbox.click(x, y):
			ssid_textbox.set_active(True, True)
		else:
			ssid_textbox.set_active(False, False)

		if passwd_textbox.click(x, y):
			passwd_textbox.set_active(True, True)
		else:
			passwd_textbox.set_active(False, False)

def key(event):
	if currentTab == 0:
		if ssid_textbox.get_active():
			ssid_textbox.key(event)
		elif passwd_textbox.get_active():
			passwd_textbox.key(event)

top.bind_all("<Key>", key)	
top.bind("<Button-1>", click)

def openMain(button):
	checkOpen(button)

def openClients(button):
	checkOpen(button)

def openAbout(button):
	checkOpen(button)

def openDebug(button):
	checkOpen(button)

strip = Label(top)
strip.place(y=4 * 32, width=32, height=128)
strip["background"] = "#37474F"

buttons[0]["command"] = lambda: openMain(0)
buttons[1]["command"] = lambda: openClients(1)
buttons[2]["command"] = lambda: openAbout(2)
buttons[3]["command"] = lambda: openDebug(3)

buttons[0].invoke()

#Add a label to the frame
#label = Label(top, text="Oh shit, what up?")
#label.pack()

#Add a button to the frame
#def killswitchEngage():
#    messagebox.showinfo("Execute Order 66", "It will be done, my lord")
#killswitch = Button(top, text="Order 66", command=killswitchEngage)
#killswitch.pack()

top.mainloop()