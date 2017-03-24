# ssid.py
# class to hold ssid info

class SSID:
	def __init__(self, name, bars, security):
		self.name = name
		self.signal = int(bars)
		self.security = security

	def get_name(self):
		return self.name

	def get_signal(self):
		return self.signal

	def get_security(self):
		return str(tuple(self.security))
	
	def __str__(self):
		return "SSID: '" + self.get_name() + "'\n ├─ SIGNAL: " + str(self.get_signal()) + "\n └─ SECURITY: " + self.get_security()
