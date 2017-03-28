# socket.py

import os
import re

class Socket:
	def __init__(self, ssid, passwd):
		#res = os.system("nmcli dev wifi con  " + ssid + " " + passwd)
		
		self.ssid = "PiRouter"
		self.passwd = None # Will be enforced to what we determined

		self.__host(self.ssid, self.passwd)
		
		#self.__enable_nat()
	
	def __host(self, ssid, passwd):
		os.system("nmcli device wifi hotspot ifname wlp7s0 ssid ayylmao password topkekayylmao")