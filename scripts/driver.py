# driver.py
# runs -- OH SHIT HERE COME DATBOI

from sock import Socket
from sniffer import Sniffer

class Driver:
	def __init__(self):
		print("Here come dat boi!")

	#Wi-Fi Kill Switch
	def order_66(self):
		print("It will be done my lord.")

	# Read Wi-Fi config (SSID/PASS)
	def __read_config(self, conf):
		try:
			my_config = open(conf, "rb")
		except FileNotFoundError:
			self.__write_config()

	# Write Wi-Fi config(SSID/PASS)
	def __write_config(self):
		#my_config = open("conf", "w+")
		my_sniffer = Sniffer()
					
		#my_config.write(my_sniffer.get_ssid() + "\n")
		#my_config.write(my_sniffer.get_psswd() + "\n")

	# Runs DATBOI
	def run(self):
		self.__read_config("config")