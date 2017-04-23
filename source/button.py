from tkinter import *

class CButton:
	def __init__(self, parent, x, y, func):
		self.x = x
		self.y = y

		self.width = 24
		self.height = 24

		self.func = func

		self.graphic = PhotoImage(file="assets/start.png")
		self.graphic_id = parent.create_image(x, y, anchor="nw", image=self.graphic)
		
		self.parent = parent

		self.pressed = False

	def click(self, x, y):
		return x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height

	def toggle(self):
		self.pressed = not self.pressed

	def get_pressed(self):
		return self.pressed

	def set_image(self, img):
		self.graphic = img
		self.parent.itemconfig(self.graphic_id, image=img)
	
	def set_color(self, r, g, b):
		fill(self.graphic, (r, g, b))

	def get_tag(self):
		return self.graphic_id