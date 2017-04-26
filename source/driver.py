# driver.py
# runs -- OH SHIT HERE COME DATBOI

import os
import signal
import subprocess

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
		self.status = 0
		self.socket = None

	#Wi-Fi Kill Switch
	def order_66(self):
		"""Toggle the WiFi radio"""

		logger.log("It will be done my lord.")
		if self.killswitch_engage:
			subprocess.check_output(["nmcli", "connection", "down", self.ssid])
			self.set_status(0)
		else:
			subprocess.check_output(["nmcli", "connection", "up", self.ssid])
			self.set_status(2)

		self.killswitch_engage != self.killswitch_engage

	def get_status(self):
		return self.status

	def set_status(self, status):
		self.status = status

	# Read Wi-Fi config (SSID/PASS)
	def __read_config(self, conf):
		"""Read config. If it fails, create one."""

		try:
			my_config = open(conf, "rb")
		except FileNotFoundError:
			self.__write_config()

	# Write Wi-Fi config(SSID/PASS)
	def write_config(self, data):
		"""
		Takes sensitive data that's been hashed
		the heck out of and write it out ¯\_(ツ)_/¯
		"""

		my_config = open("config.datboi", "w+")
		my_config.write(json.dumps(data, sort_keys=True, indent=4))

	def set_error(self, field, valid_err=0):
		error_string = None
		if valid_err == -1:
			error_string = "Field required"
		elif valid_err == -2:
			error_string = "Length must be at least 14 characters"
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
			self.set_status(1)
			self.socket = Socket(ssid, passwd, self)
	
	def get_socket(self):
		return self.socket