# socket.py

import os
import re
import signal
import subprocess
import sys

class Socket:
	def __init__(self, ssid, passwd):
		#res = os.system("nmcli dev wifi con  " + ssid + " " + passwd)
		
		self.ssid = "PiRouter"
		self.passwd = None # Will be enforced to what we determined

		self.__add_iw()
	
	def __add_iw(self):
		os.system("dmesg | grep wlan0 > ./hotspot/ifname")
		dev_str = open("./hotspot/ifname", "rb").read().decode("utf-8")
		dev = re.search("(\w+): ", dev_str).group(1)
		os.system("sudo iw dev " + dev + " interface add " + self.ssid + " type station")
		os.system("nmcli device wifi hotspot ifname " + dev + " con-name " + dev + " ssid " + dev + " password " + self.passwd)