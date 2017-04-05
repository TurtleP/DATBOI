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
		print("\n[Getting WiFi Information]\n")
		start_time = time.time()

		dmesg = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
		grep = subprocess.Popen(["grep", "wlan0"], stdin=dmesg.stdout, stdout=subprocess.PIPE)
		dmesg.stdout.close()
		dev = re.search("(\w+): ", grep.communicate()[0].decode("utf-8")).group(1)
		
		print("[" + str(round(time.time() - start_time, 3)) + "] :: WiFi Device: " + dev)

		print("[" + str(round(time.time() - start_time, 3)) + "] :: Adding virtual network: " + self.ssid)
		
		try:
			print("") #subprocess.Popen(["iw", "dev", dev, "interface", "add", self.ssid, "type", "station"])
		except OSError:
			print("[" + str(round(time.time() - start_time, 3)) + "] :: Virtual network alrady created.")
		
		bssid_proccess = subprocess.Popen(["iw", dev, "scan"], stdout=subprocess.PIPE)
		egrep_bssid = subprocess.Popen(["egrep", "^BSS|SSID:"], stdin=bssid_proccess.stdout, stdout=subprocess.PIPE)
		egrep_associated = subprocess.Popen(["egrep", "associated"], stdin=egrep_bssid.stdout, stdout=subprocess.PIPE)

		bssid_proccess.stdout.close()
		egrep_bssid.stdout.close()
		bssid = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", egrep_associated.communicate()[0].decode("utf-8")).group(0).upper()

		print("[" + str(round(time.time() - start_time, 3)) + "] :: Acess Point BSSID: " + bssid)

		ifconfig_process = subprocess.Popen(["ifconfig", self.ssid], stdout=subprocess.PIPE)
		ether_egrep = subprocess.Popen(["egrep", "ether"], stdin=ifconfig_process.stdout, stdout=subprocess.PIPE)

		ifconfig_process.stdout.close()
		mac_addr = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", ether_egrep.communicate()[0].decode("utf-8")).group(0).upper()

		print("[" + str(round(time.time() - start_time, 3)) + "] :: Cloned MAC Address: " + mac_addr)

		print("[" + str(round(time.time() - start_time, 3)) + "] :: Creating connection")

		command =  "nmcli connection add "
		command += "connection.id Memes " 
		command += "connection.interface-name " + self.ssid + " "
		command += "connection.type 802-11-wireless "
		
		command += "802-11-wireless.ssid " + self.ssid + " " 
		command += "802-11-wireless.mode ap "
		command += "802-11-wireless.bssid '" + bssid + "' "
		command += "802-11-wireless.cloned-mac-address '" + mac_addr + "' "
		command += "802-11-wireless-security.key-mgmt wpa-psk "
		command += "802-11-wireless-security.wep-key0 OHSHITWADDUP "
		command += "802-11-wireless-security.psk OHSHITWADDUP "
		
		command += "ipv4.method shared"

		print("[" + str(round(time.time() - start_time, 3)) + "] :: Connection added.")