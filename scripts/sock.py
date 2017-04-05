# socket.py

import os
import re
import signal
import subprocess
import sys
import time

class Socket:
	def __init__(self, ssid, passwd):
		#res = os.system("nmcli dev wifi con  " + ssid + " " + passwd)
		
		self.ssid = "PiRouter"
		self.passwd = None # Will be enforced to what we determined

		self.__add_iw()
	
	def __add_iw(self):
		os.system("dmesg | grep wlan0 > ./hotspot/data")
		dev_str = open("./hotspot/data", "rb")
		dev = re.search("(\w+): ", dev_str.read().decode("utf-8")).group(1)
		dev_str.close()
		
		print(":: Wifi Device: " + dev)

		time.sleep(1)

		print(":: Adding virtual network: " + self.ssid)
		
		#os.system("sudo iw dev " + dev + " interface add " + self.ssid + " type station")
		
		time.sleep(1)

		os.system("sudo iw " + dev + " scan | egrep '^BSS|SSID:' | egrep 'associated' > ./hotspot/data")

		bssid_str = open("./hotspot/data", "rb")
		bssid = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", bssid_str.read().decode("utf-8")).group(0)
		bssid_str.close()

		print(":: Acess Point BSSID: " + bssid)

		command =  "nmcli connection add"
		command += "connection.id Memes" 
		command += "connection.interface-name wlp7s1"
		command += "connection.type 802-11-wireless"
		
		command += "802-11-wireless.ssid DATBOI" 
		command += "802-11-wireless.mode ap"
		command += "802-11-wireless.bssid '18:64:72:8C:3D:E0'"
		command += "802-11-wireless.cloned-mac-address '24:FD:52:F8:F8:B9'"
		command += "802-11-wireless-security.key-mgmt wpa-psk"
		command += "802-11-wireless-security.wep-key0 OHSHITWADDUP"
		command += "802-11-wireless-security.psk OHSHITWADDUP"
		
		command += "ipv4.method shared"