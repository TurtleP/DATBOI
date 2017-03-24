# sniffer.py
# SSID sniffer

import os
import signal
import subprocess
import sys
import re

from ssid import SSID

class Sniffer:
	def __init__(self):
		self.ssids = []
		self.__sniff_ssids()
	
	# Sniff SSIDS
	def __sniff_ssids(self):
		nmcliProc = subprocess.Popen(['nmcli', '-t', '-f', 'SSID, SIGNAL, SECURITY', 'device', 'wifi', 'list'], stdout=subprocess.PIPE)
		
		for line in nmcliProc.stdout:
			fields = list(line.decode('utf-8').split(":"))

			if fields[0] == "--":
				fields[0] = "Hidden"

			if fields[2] == "\n":
				fields[2] = "OPEN"
			else:
				fields[2] = re.sub("\n", "", fields[2])
			
			self.ssids.append(SSID(fields[0], fields[1], fields[2].split(" ")))

		nmcliProc.kill()
		self.display_ssids()

	def __filter(self, ssid):
		if ssid.get_signal() < 35:
			return False
		
		for i in range(len(self.ssids)):
			if self.ssids[i].get_signal() > ssid.get_signal():
				return True
			else:
				return False

	def display_ssids(self):
		for i in range(len(self.ssids)):
			if self.__filter(self.ssids[i]):
				print(str(self.ssids[i]) + "\n")
	
	def get_ssid(self):
		return input("SSID: ")

	def get_psswd(self):
		return input("Pass: ")