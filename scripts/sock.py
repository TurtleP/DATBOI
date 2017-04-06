# socket.py

import os
import re
import signal
import subprocess
import sys
import time

class Socket:
	def __init__(self, ssid, passwd):
		"""
		Initialize the Socket
		@ssid: SSID to connect to
		@passwd: Router password
		"""
		
		self.ssid = "PiRouter"
		self.passwd = "HERECOMEDATBOI" # Will be enforced to what we determined
		self.dev = None

		self.start_time = time.time()

		self.__add_iw()
	
	def __add_iw(self):
		"""Creates a virtual interface bound to wlan0"""

		print("\n[Getting WiFi Information]\n")

		dmesg = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
		grep = subprocess.Popen(["grep", "wlan0"], stdin=dmesg.stdout, stdout=subprocess.PIPE)
		dmesg.stdout.close()
		self.dev = re.search("(\w+): ", grep.communicate()[0].decode("utf-8")).group(1)
		
		print("[" + str(round(time.time() - self.start_time, 3)) + "] :: WiFi Device: " + self.dev)

		try:
			print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Adding virtual network: " + self.ssid)
			subprocess.check_output(["iw", "dev", self.dev, "interface", "add", self.ssid, "type", "station"])
		except (subprocess.CalledProcessError, OSError):
			print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Virtual network alrady created.")
			
		self.__create_hotspot()

	def __create_hotspot(self):
		"""Finds associated MAC addresses. Creates a hotspot."""

		bssid_proccess = subprocess.Popen(["iw", self.dev, "scan"], stdout=subprocess.PIPE)
		egrep_bssid = subprocess.Popen(["egrep", "^BSS|SSID:"], stdin=bssid_proccess.stdout, stdout=subprocess.PIPE)
		egrep_associated = subprocess.Popen(["egrep", "associated"], stdin=egrep_bssid.stdout, stdout=subprocess.PIPE)

		bssid_proccess.stdout.close()
		egrep_bssid.stdout.close()
		bssid = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", egrep_associated.communicate()[0].decode("utf-8")).group(0).upper()

		print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Acess Point BSSID: " + bssid)

		ifconfig_process = subprocess.Popen(["ifconfig", self.ssid], stdout=subprocess.PIPE)
		ether_egrep = subprocess.Popen(["egrep", "ether"], stdin=ifconfig_process.stdout, stdout=subprocess.PIPE)

		ifconfig_process.stdout.close()
		mac_addr = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", ether_egrep.communicate()[0].decode("utf-8")).group(0).upper()

		print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Cloned MAC Address: " + mac_addr)

		print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Creating connection")

		try:	
			print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Connection added.")
			subprocess.check_output(["nmcli", "connection", "add", "connection.id", self.ssid, "connection.id", self.ssid, "connection.interface-name", self.ssid, "connection.type", "802-11-wireless", "802-11-wireless.ssid", self.ssid, "802-11-wireless.mode", "ap", "802-11-wireless.bssid", bssid, "802-11-wireless.cloned-mac-address", mac_addr, "802-11-wireless-security.key-mgmt", "wpa-psk", "802-11-wireless-security.wep-key0", self.passwd, "802-11-wireless-security.psk", self.passwd, "ipv4.method", "shared"])
		except (subprocess.CalledProcessError, OSError):
			print("[" + str(round(time.time() - self.start_time, 3)) + "] :: Connection already exists!")