# driver.py
# runs -- OH SHIT HERE COME DATBOI
import os
import signal
import subprocess
import sys
import re

from sock import Socket
from ssid import SSID

class Driver:
	def __init__(self):
		print("Here come dat boi!")
		self.ssids = []

	#Wi-Fi Kill Switch
	def order_66(self):
		print("It will be done my lord.")

	# Read Wi-Fi config (SSID/PASS)
	def __read_config(self, conf):
		try:
			my_config = open(conf, "rb")
			print(my_config.read())
		except IOError:
			self.__write_config()

	# Write Wi-Fi config(SSID/PASS)
	def __write_config(self):
		my_config = open("conf", "w+")

		for i in range(len(self.ssids)):
			print(str(self.ssids[i]) + "\n")
					
		ssid_input = input("Enter SSID: ")
		my_config.write(ssid_input + "\n")
		pass_input = input("Enter Pass: ")
		my_config.write(pass_input)

	def __sniff_ssids(self):
		p = subprocess.Popen(['nmcli', '-t', '-f', 'SSID, SIGNAL, SECURITY', 'device', 'wifi', 'list'], stdout=subprocess.PIPE)
		
		ssid_list = []
		for line in p.stdout:
			fields = line.decode('utf-8').split(":")
			ssid_list.append(fields)

		p.kill()

		ssid_list.pop(0)
		for i in range(len(ssid_list)):
			if ssid_list[i][2] == "\n":
				ssid_list[i][2] = "OPEN"
			else:
				ssid_list[i][2] = re.sub("\n", "", ssid_list[i][2])

			self.ssids.append(SSID(ssid_list[i][0], ssid_list[i][1], ssid_list[i][2].split(" ")))

	# Runs DATBOI
	def run(self):
		self.__sniff_ssids()
		self.__read_config("config")