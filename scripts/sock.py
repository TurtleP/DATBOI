# socket.py
# TCP Socket Connection
import socket

class Socket:
	def __init__(self):
		print("init..")
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("stream socket made!")