# sniffer.py
# SSID sniffer

import os
import signal
import subprocess
import sys
import re
import pydoc

pydoc.importfile("ssid.py")

from ssid import SSID

class Sniffer:
	def __init__(self):
		"""Initialize the sniffer"""

		self.ssids = dict()
		self.__sniff_ssids()
	
	# Sniff SSIDS
	def __sniff_ssids(self):
		"""Use 'nmcli' with terse output to find SSID listings"""

		nmcliProc = subprocess.Popen(['nmcli', '-t', '-f', 'SSID, SIGNAL, SECURITY', 'device', 'wifi', 'list'], stdout=subprocess.PIPE)
		
		for line in nmcliProc.stdout:
			fields = list(line.decode('utf-8').split(":"))

			try:
				if fields[0] == "--":
					fields[0] = "Hidden"

				if fields[2] == "\n":
					fields[2] = "OPEN"
				else:
					fields[2] = re.sub("\n", "", fields[2])
			
				if not fields[0] in self.ssids:
					self.ssids[fields[0]] = list()

				self.ssids[fields[0]].append(SSID(fields[0], fields[1], fields[2].split(" ")))
			except IndexError:
				print("")
				
		nmcliProc.kill()
		self.display_ssids()

	def display_ssids(self):
		"""Show the list of captured SSIDs"""

		for name in self.ssids:
			self.ssids[name].sort(key=lambda x:name, reverse=True)
		
		for name in self.ssids:
			print(name + " " + self.ssids[name][0].get_security() + " -> " + str(self.ssids[name][0].get_signal()))
			
	def get_ssid(self):
		"""Get input for the SSID and return it"""

		return input("SSID: ")

	def get_psswd(self):
		"""Get input for the router password and return it"""

		return input("Pass: ")