# ssid.py
# class to hold ssid info

class SSID:
	def __init__(self, name, bars, security):
		"""
		Initialize a new SSID object
		@name: name of the SSID
		@bars: signal strength of SSID
		@security: security type (WEP/WEP2/802.11)
		"""

		self.name = name
		self.signal = int(bars)
		self.security = security

	def get_name(self):
		"""Return SSID"""

		return self.name

	def get_signal(self):
		"""Return signal strength"""

		return self.signal

	def get_security(self):
		"""Return security type as a tuple"""
		
		return str(tuple(self.security))
	
	def __str__(self):
		return "SSID: '" + self.get_name() + "'\n ├─ SIGNAL: " + str(self.get_signal()) + "\n └─ SECURITY: " + self.get_security()
