# driver.py
# runs -- OH SHIT HERE COME DATBOI

import os
from sock import Socket
from sniffer import Sniffer

class Driver:
	def __init__(self):
		print("Here come dat boi!")
		self.killswitch_engage = True

	#Wi-Fi Kill Switch
	def order_66(self):
		print("It will be done my lord.")
		if self.killswitch_engage:
			os.system("nmcli radio wifi off")
		else:
			os.system("nmcli radio wifi on")

		self.killswitch_engage != self.killswitch_engage

	# Read Wi-Fi config (SSID/PASS)
	def __read_config(self, conf):
		try:
			my_config = open(conf, "rb")
		except FileNotFoundError:
			self.__write_config()

	# Write Wi-Fi config(SSID/PASS)
	def __write_config(self):
		my_config = open("conf", "w+")
		my_sniffer = Sniffer()
		
		ssid, passwd = my_sniffer.get_ssid(), my_sniffer.get_psswd()
		my_config.write(ssid + "\n")
		my_config.write(passwd + "\n")

		Socket(ssid, passwd)
	
	# Runs DATBOI
	def run(self):
		Socket("idk", "lel")