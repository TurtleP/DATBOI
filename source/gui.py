from tkinter import *
from textbox import TextBox
from button import CButton
from driver import Driver
from init import logger
from client import Client
import json
import re
import subprocess

DATBOI = Driver()

# Define the frame
top = Tk()
top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(400, 256)) # Formatted as W * H
top.wm_title("DATBOI v0.8.0")
top["background"] = "#263238"

buttons = []

graphics = [] # Button graphics
graphics.append(PhotoImage(file="assets/gears.png"))
graphics.append(PhotoImage(file="assets/wifi.png"))
graphics.append(PhotoImage(file="assets/about.png"))
graphics.append(PhotoImage(file="assets/debug.png"))

search_image = PhotoImage(file="assets/search.png")

# Canvas items
canvas_items = list()

# Logo thing
datBoi = PhotoImage(file="assets/datboi.png")

# Create tab buttons
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

# Create canvas to render on
renderCanvas = Canvas(top, highlightthickness=0)
renderCanvas["background"] = "#263238"
renderCanvas.place(x=32, width=368, height=256)

# Current tab
currentTab = 0

# Automated fun stuff. Disable all other button 
# elements from showing except the current tab
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

# Add an item with its ID from the 
# canvas to the object array
def add_item(item, indx=currentTab):
	canvas_items[indx].append(item)

####MAIN TAB
renderCanvas.create_image(270, 130, image=datBoi)

add_item(renderCanvas.create_text(30, 4, fill="#FFFFFF", text="Access Point Configuration", anchor="nw", font=("assets/Roboto-Regular", 18, "normal")))
	
ssid_textbox = TextBox(renderCanvas, 112, 80, 144, "SSID Name")
passwd_textbox = TextBox(renderCanvas, 112, 145, 144, "Password", True)

for item in ssid_textbox.get_items():
	add_item(item)

for item in passwd_textbox.get_items():
	add_item(item)

def load_DATBOI():
	ssid_is_valid = DATBOI.validate(ssid_textbox)
	pass_is_valid = DATBOI.validate(passwd_textbox)

	if ssid_is_valid and pass_is_valid:
		start_button.toggle()

		if DATBOI.get_status() == 0:
			if start_button.get_pressed():
				start_button.set_image(stop_button)
				
				ssid, passwd = ssid_textbox.get_text(), passwd_textbox.get_text()

				DATBOI.run(ssid, passwd)
		elif DATBOI.get_status() == 2:
			start_button.set_image(start_graphic)
			DATBOI.order_66()

start_button = CButton(renderCanvas, 172, 210, load_DATBOI)
add_item(start_button.get_tag())

start_graphic = PhotoImage(file="assets/start.png")
stop_button = PhotoImage(file="assets/stop.png")
###END MAIN

###CONNECTIONS PAGE
add_item(renderCanvas.create_text(72, 4, fill="#FFFFFF", text="Connected Devices", anchor="nw", font=("assets/Roboto-Regular", 18, "normal")), 1)

client_text = renderCanvas.create_text(4, 48, fill="#FFFFFF", text="", anchor="nw", font=("assets/Roboto-Regular.ttf", 12, "normal"))
add_item(client_text, 1)

connections = list()
blacklist = list()
#ssid_textbox.set_text("DATBOI")
def update_clients():
	sp = None
	client_output_text = "No connections found"

	client_output = list()
	if ssid_textbox.get_text() != "":
		sp = subprocess.Popen(["arp", "-i", ssid_textbox.get_text()], stdout=subprocess.PIPE)
		awk = subprocess.Popen(["awk", '{ print $1"-"$3 }'], stdin=sp.stdout, stdout=subprocess.PIPE)

		for line in awk.stdout:
			data = list(line.decode("utf-8").split("-"))

			if re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|\w+\.\w+\.\w+", data[0]) and re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", data[1]):
				data[1] = re.sub("\n", "", data[1])
				client_output.append([data[0], data[1]])
	 
	if len(client_output) > 0:
		for i in range(len(connections)):
			connections[i].clear()
		del connections[0:]

		if currentTab == 1:
			if len(blacklist) > 0:
				for i in range(len(blacklist)):
					temp_client = Client(renderCanvas, 6, 48 + (i * 32), blacklist[i][0], blacklist[i][1], True, DATBOI.get_socket().get_mac_addr())
					connections.append(temp_client)

			for i in range(len(client_output)):
				passd = True

				if len(blacklist) > 0:
					if blacklist[i][1] == client_output[i][1]:
						passd = False

				if passd:
					temp_client = Client(renderCanvas, 6, 48 + ((len(blacklist) + i) * 32), client_output[i][0], client_output[i][1])
					connections.append(temp_client)

			client_output_text = ""
	else:
		client_output_text = "No connections found"

	renderCanvas.itemconfig(client_text, text=client_output_text)

	top.after(1000, update_clients)

update_clients()
###END CONNECTIONS PAGE

###ABOUT PAGE

add_item(renderCanvas.create_text(4, 0.5, fill="#FFFFFF", text="DATBOI", anchor="nw", font=("assets/Roboto-Regular.ttf", 24, "normal")), 2)
add_item(renderCanvas.create_text(135, 4, fill="#FFFFFF", text="Device Allowing Transfer Between\nOther Internet Devices", anchor="nw", font=("assets/Roboto-Regular.ttf", 10, "normal")), 2)
authors = [
	"Asad Arif",
	"Colby Outcalt",
	"Curtis Parker",
	"Jeremy Postelnek",
	"Nicholas-Roache",
]
for i in range(len(authors)):
	add_item(renderCanvas.create_text(4, 70 + (i * 24), fill="#FFFFFF", text="• " + authors[i], anchor="nw", font=("assets/Roboto-Regular.ttf", 14, "normal")), 2)
add_item(renderCanvas.create_text(4, 224, fill="#FFFFFF", text="This code is licensed under the MIT Open Source\nLicense. © 2017 DATBOI Inc.", anchor="nw", font=("assets/Roboto-Regular.ttf", 10, "normal")), 2)

###END ABOUT PAGE

####DEBUG TAB
add_item(renderCanvas.create_image(4, 4, anchor="nw", image=search_image), 3)
debug_id = renderCanvas.create_text(4, 32, fill="#FFFFFF", text=logger.get_logs(), anchor="nw", font=("assets/Roboto-Regular.ttf", 10, "normal"))
add_item(debug_id, 3)

def update_logs():
	renderCanvas.itemconfig(debug_id, text=logger.get_logs())
	top.after(1000, update_logs)

search_textbox = TextBox(renderCanvas, 24, 4, 120, "Filter", False, 10)
for item in search_textbox.get_items():
	add_item(item, 3)

update_logs()
####END DEBUG

# Left click mouse events
def click(event):
	x, y = event.x, event.y
	if currentTab == 0:
		if ssid_textbox.click(x, y):
			ssid_textbox.set_active(True, True)
		else:
			ssid_textbox.set_active(False, False)

		if passwd_textbox.click(x, y):
			passwd_textbox.set_active(True, True)
		else:
			passwd_textbox.set_active(False, False)
		
		if start_button.click(x, y):
			start_button.func()
	elif currentTab == 1:
		for i in range(len(connections)):
			try:
				if connections[i].click(x, y):
					if not connections[i].get_kicked():
						blacklist.append([connections[i].hostname, connections[i].get_mac()])
						
						with open("blacklist.txt", "w") as outfile:
							json.dump(blacklist, outfile, indent=4)
					else:
						blacklist.pop(i)
					
					#client=subprocess.Popen(["arp-scan", "-I", DATBOI.get_socket().get_interface(), "-l"], stdout=subprocess.PIPE)
					#mac_addr = subprocess.Popen(["grep", "-m", "1", connections[i].get_mac()], stdin=client.stdout, stdout=subprocess.PIPE)
					#print(mac_addr.communicate()[0].decode("utf-8"))
					
					connections[i].get_button().func()
					connections.pop(i)
			except IndexError:
				print("Index error")

	elif currentTab == 3:
		if search_textbox.click(x, y):
			search_textbox.set_active(True, True)
		else:
			search_textbox.set_active(False, False)

# Keybinding events
def key(event):
	if currentTab == 0:
		if ssid_textbox.get_active():
			ssid_textbox.key(event)
		elif passwd_textbox.get_active():
			passwd_textbox.key(event)
	elif currentTab == 3:
		if search_textbox.get_active():
			search_textbox.key(event)
			if search_textbox.get_length() > 0:
				logger.filter(search_textbox.get_text())
			else:
				logger.clear_filter()

top.bind_all("<Key>", key)	
top.bind("<Button-1>", click)

# Tab opening functions
def openMain(button):
	checkOpen(button)

def openClients(button):
	checkOpen(button)

def openAbout(button):
	checkOpen(button)

def openDebug(button):
	checkOpen(button)

# Spacing stuff for fanciness
strip = Label(top)
strip.place(y=4 * 32, width=32, height=128)
strip["background"] = "#37474F"

# Set button commands
buttons[0]["command"] = lambda: openMain(0)
buttons[1]["command"] = lambda: openClients(1)
buttons[2]["command"] = lambda: openAbout(2)
buttons[3]["command"] = lambda: openDebug(3)

# Open to the Main tab by default
buttons[0].invoke()

# Run the main window
top.mainloop()
