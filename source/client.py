# client.py
# client from a listing in nbtscan

from tkinter import *
from button import CButton
from tkinter import messagebox

class Client:
	def __init__(self, parent, x, y, hostname, mac=None, ip=None):
		self.hostname = hostname
		self.mac_addr = mac
		self.ip_addr = ip

		self.graphic = PhotoImage(file="assets/device.png")

		self.parent = parent 

		self.button = CButton(self.parent, x, y, lambda: messagebox.askyesno("Kick Device", "Kick client " + hostname + "?"))
		self.button.set_image(self.graphic)

		parent.create_text(x + 32, y + 3, fill="#FFFFFF", anchor="nw", text=hostname, font=("assets/Roboto-Regular.ttf", 12, "normal"))

	def click(self, x, y):
		return self.button.click(x, y)

	def get_button(self):
		return self.button