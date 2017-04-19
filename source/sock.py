# socket.py

import os
import re
import signal
import subprocess
import sys
import time

from init import logger

class Socket:
	def __init__(self, ssid, passwd):
		"""
		Initialize the Socket
		@ssid: SSID to connect to
		@passwd: Router password
		"""
		
		self.ssid = ssid
		self.passwd = passwd # Will be enforced to what we determined
		self.dev = None

		self.start_time = time.time()

		self.__add_iw()
	
	def __add_iw(self):
		"""Creates a virtual interface bound to wlan0"""

		logger.log("Getting WiFi Information")

		dmesg = subprocess.Popen(["dmesg"], stdout=subprocess.PIPE)
		grep = subprocess.Popen(["grep", "wlan0"], stdin=dmesg.stdout, stdout=subprocess.PIPE)
		dmesg.stdout.close()
		self.dev = re.search("(wlan0): ", grep.communicate()[0].decode("utf-8")).group(1)
		
		logger.log(":: WiFi Device: " + self.dev)

		try:
			logger.log(":: Adding virtual network: " + self.ssid)
			subprocess.check_output(["iw", "dev", self.dev, "interface", "add", self.ssid, "type", "__ap"])
		except (subprocess.CalledProcessError, OSError):
			logger.log(":: Couldn't add virtual network: already exists.")
			
		self.__create_hotspot()

	def __create_hotspot(self):
		"""Finds associated MAC addresses. Creates a hotspot."""
		connections = subprocess.Popen(["nmcli", "connection"], stdout=subprocess.PIPE)
		conn_grep = subprocess.Popen(["grep", self.ssid], stdin=connections.stdout, stdout=subprocess.PIPE)
			
		connections.stdout.close()
		if not re.search("\w+", conn_grep.communicate()[0].decode("utf-8")) is None:
			logger.log(":: Connection already exists. Starting..")
			try:
				subprocess.check_output(["nmcli", "connection", "up", self.ssid])
			except subprocess.CalledProcessError:
				logger.log(":: Failed to start hotspot " + self.ssid)
		else:
			bssid_proccess = subprocess.Popen(["iw", self.dev, "scan"], stdout=subprocess.PIPE)
			egrep_bssid = subprocess.Popen(["egrep", "^BSS|SSID:"], stdin=bssid_proccess.stdout, stdout=subprocess.PIPE)
			egrep_associated = subprocess.Popen(["egrep", "associated"], stdin=egrep_bssid.stdout, stdout=subprocess.PIPE)

			bssid_proccess.stdout.close()
			egrep_bssid.stdout.close()
			bssid = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", egrep_associated.communicate()[0].decode("utf-8")).group(0).upper()

			logger.log(":: Acess Point BSSID: " + bssid)

			ifconfig_process = subprocess.Popen(["ifconfig", self.ssid], stdout=subprocess.PIPE)
			ether_egrep = subprocess.Popen(["egrep", "HWaddr"], stdin=ifconfig_process.stdout, stdout=subprocess.PIPE)

			ifconfig_process.stdout.close()
			mac_addr = re.search("(([a-f0-9]{2}:){5}([a-f0-9]{2}))", ether_egrep.communicate()[0].decode("utf-8")).group(0).upper()

			logger.log(":: Cloned MAC Address: " + mac_addr)

			logger.log(":: Creating connection..")

			try:	
				logger.log(":: Connection added.")
				subprocess.check_output(["nmcli", "connection", "add", "connection.id", self.ssid, "connection.interface-name", self.ssid, "connection.autoconnect", "true", "connection.type", "802-11-wireless", "802-11-wireless.ssid", self.ssid, "802-11-wireless.mode", "ap", "802-11-wireless.bssid", bssid, "802-11-wireless.cloned-mac-address", mac_addr, "802-11-wireless-security.key-mgmt", "wpa-psk", "802-11-wireless-security.wep-key0", self.passwd, "802-11-wireless-security.psk", self.passwd, "802-11-wireless-security.wep-key-type", "2", "ipv4.method", "shared"])
			except (subprocess.CalledProcessError, OSError):
				logger.log(":: Connection already exists!")

		try:
			config = subprocess.Popen(["iwconfig", self.ssid], stdout=subprocess.PIPE).communicate()[0].decode("utf-8")
			if re.search("Master", config) is None:
				logger.log("Failed to connect")
			else:
				logger.log("Connection successful")
		except subprocess.CalledProcessError:
			logger.log(":: Failed to start hotspot " + self.ssid)

