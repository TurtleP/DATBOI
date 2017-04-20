# driver.py
# runs -- OH SHIT HERE COME DATBOI

import os
import signal
import subprocess
import encryption

from sock import Socket
from sniffer import Sniffer
from init import logger

class Driver:
	def __init__(self):
		"""Initialize DATBOI"""

		self.killswitch_engage = True
		self.VALIDATION_ERRORS = {
			"ERR_EMPTY": -1,
			"ERR_LENGTH": -2,
			"ERR_INSECURE": -3
		}
		logger.log("Here come DATBOI")
		self.ssid = None

	#Wi-Fi Kill Switch
	def order_66(self):
		"""Toggle the WiFi radio"""

		logger.log("It will be done my lord.")
		if self.killswitch_engage:
			subprocess.check_output(["nmcli", "connection", "down", self.ssid])
		else:
			subprocess.check_output(["nmcli", "connection", "up", self.ssid])

		self.killswitch_engage != self.killswitch_engage

	# Read Wi-Fi config (SSID/PASS)
	def __read_config(self, conf):
		"""Read config. If it fails, create one."""

		try:
			my_config = open(conf, "rb")
		except FileNotFoundError:
			self.__write_config()

	# Write Wi-Fi config(SSID/PASS)
	def __write_config(self):
		"""
		Asks for input and creates a new config
		with this data (SSID, PASSWD)
		"""

		my_config = open("conf", "w+")
		my_sniffer = Sniffer()

	def set_error(self, field, valid_err=0):
		error_string = None
		if valid_err == -1:
			error_string = "Field required"
		elif valid_err == -2:
			error_string = "Length must be between 14-20 characters"
		elif valid_err == -3:
			error_string = "Insecure passphrase"
	
		if not error_string is None:
			logger.log(error_string)
			field.error(error_string)
			return False
		field.clear_error()
		return True

	def validate(self, field):
		if field.get_text() == "" or field.get_text() is None:
			return self.set_error(field, self.VALIDATION_ERRORS["ERR_EMPTY"])
		elif field.is_passwd(): 
			if field.get_length() < 14:
				return self.set_error(field, self.VALIDATION_ERRORS["ERR_LENGTH"]) 
		return self.set_error(field)

	# Runs DATBOI
	def run(self, ssid=None, passwd=None):
		"""OH SNAP HERE COME DATBOI"""
		logger.log("Starting DATBOI..")
		if (ssid == "" or ssid is None) and (passwd == "" or passwd is None):
			return self.VALIDATION_ERRORS["ERR_EMPTY"]
		else:
			self.ssid = ssid
			Socket(ssid, setPassword(passwd))
