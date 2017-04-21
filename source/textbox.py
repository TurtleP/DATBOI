# textbox.py

from tkinter import *
import re

class TextBox:
	def __init__(self, parent, x, y, width, hint, passwd=False, maxlen=13):
		self.x = x
		self.y = y
		self.width = width
		self.height = 16

		self.error_image = PhotoImage(file="assets/error_text.png")
		self.active_image = PhotoImage(file="assets/keyboard.png")
		self.inactive_image = PhotoImage(file="assets/none.png")

		self.text = ""
		self.hint = hint

		self.maxlen = maxlen

		self.parent = parent
		self.highlight = False

		self.passwd = passwd

		self.underline_id = parent.create_line(x, y + 16, x + width, y + 16, fill="#37474F")
		self.id = parent.create_text(x, y + 8, anchor="w", fill="#9E9E9E", text=hint, font=("assets/Roboto-Regular.ttf", 12, "normal"))
		self.error_id = parent.create_text(x, y + 24, anchor="w", fill="#E53935", text="", font=("assets/Roboto-Regular.ttf", 8, "normal"))
		self.icon_image_id = self.parent.create_image(self.x + self.width - 8, self.y + 8, image=self.inactive_image)

	def key(self, event):	
		if event.keysym == "BackSpace":
			self.text = self.text[:-1]

			color = "#FFFFFF"
			text = self.text
			
			if self.passwd:
				text = re.sub("\w", "*", self.text)
			
			if len(self.text) == 0:
				color="#9E9E9E"
				text = self.hint

			self.parent.itemconfig(self.id, fill=color, text=text)
		elif event.keysym == "Escape" or event.keysym == "Return":
			self.set_status(self.inactive_image)
			self.highlight = False

		if len(self.text) > self.maxlen or not self.highlight:
			return

		if event.char == event.keysym or event.char == " ":
			self.text += event.char

			text = self.text
			if self.passwd:
				text = re.sub("\w", "*", self.text)

			self.parent.itemconfig(self.id, fill="#FFFFFF", text=text)

	def click(self, x, y):
		return x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height
	
	def set_active(self, highlight, status):
		self.highlight = highlight
		if status:
			self.set_status(self.active_image)
		else:
			self.set_status(self.inactive_image)

	def get_length(self):
		return len(self.text)

	def is_passwd(self):
		return self.passwd

	def get_active(self):
		return self.highlight

	def get_items(self):
		return (self.id, self.underline_id, self.error_id, self.icon_image_id)

	def get_text(self):
		return self.text

	def clear_error(self):
		self.parent.itemconfig(self.error_id, text="")
		self.set_status(self.inactive_image)

	def error(self, text):
		self.parent.itemconfig(self.error_id, text=text)
		self.set_status(self.error_image)

	def set_status(self, img):
		self.parent.itemconfig(self.icon_image_id, image=img)