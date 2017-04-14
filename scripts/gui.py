from tkinter import *

#Define the frame
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(400, 256)) #Formatted as W * H
top.wm_title("Here Come DATBOI!")
top["background"] = "#263238"

buttons = []

graphics = []
graphics.append(PhotoImage(file="assets/gears.png"))
graphics.append(PhotoImage(file="assets/wifi.png"))
graphics.append(PhotoImage(file="assets/about.png"))
graphics.append(PhotoImage(file="assets/debug.png"))

canvas_elements = []

datBoi = PhotoImage(file="assets/datboi.png")

for i in range(len(graphics)):
	configButton = Button(top, border=0, highlightthickness=0)
	configButton["background"] = "#37474F"
	configButton["activebackground"] = "#37474F"
	configButton["highlightbackground"] = "#37474F"
	configButton["relief"] = "flat"
	configButton.config(image=graphics[i])
	configButton.place(rely=i/8, width=32, height=32)
	buttons.append(configButton)

renderCanvas = Canvas(top, highlightthickness=0)
renderCanvas["background"] = "#263238"
renderCanvas.place(x=32, width=368, height=256)

ssid_text = ""
currentTab = 1

def checkOpen(button):
	for i in range(len(graphics)):
		if i != button:
			buttons[i]["background"] = "#37474F"
			buttons[i]["activebackground"] = "#37474F"
		else:
			buttons[button]["background"] = "#263238"
			buttons[button]["activebackground"] = "#263238"
			currentTab = i
	
	renderCanvas.delete(ALL)
	renderCanvas.create_image(270, 130, image=datBoi)

def key(event):
	if event.char == event.keysym:
		if currentTab == 1:
			renderCanvas.delete(canvas_elements[0])
			ssid_text += event.char
			canvas_elements[0] = renderCanvas.create_text(158, 80, fill="#FFFFFF", text=ssid_text, font=("Roboto Regular", 12, "normal"))

top.bind_all('<Key>', key)

def motion(event):
	x, y = event.x, event.y

top.bind('<Motion>', motion)

def clicked(event):
	x, y = event.x, event.y

top.bind("<Button-1>", clicked)

def openMain(button):
	checkOpen(button)

	renderCanvas.create_text(180, 24, fill="#FFFFFF", text="Acess Point Configuration", font=("Roboto Regular", 18, "normal"))
	
	canvas_elements.append(renderCanvas.create_text(158, 80, fill="#FAFAFA", text="SSID Name", font=("Roboto Regular", 12, "normal")))
	renderCanvas.create_line(112, 89, 256, 89, fill="#37474F")

def openClients(button):
   checkOpen(button)

def openAbout(button):
	checkOpen(button)

def openDebug(button):
	checkOpen(button)

strip = Label(top)
strip.place(y=4 * 32, width=32, height=124)
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