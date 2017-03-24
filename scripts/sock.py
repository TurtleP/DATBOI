# socket.py

import os

class Socket:
	def __init__(self, ssid, passwd):
		res = os.system("nmcli dev wifi con  " + ssid + " " + passwd)
		self.ssid = "PiRoute"
		os.execute("ifconfig wifi up 10.0.0.1 netmask 255.255.255.0")
		
		self.__enable_nat()
	
	def __enable_nat(self):
		os.execute("iptables --flush")
		os.execute("iptables --table nat --flush")
		os.execute("iptables --delete-chain")
		os.execute("iptables --table nat --delete-chain")
		os.execute("iptables --table nat --append POSTROUTING --out-interface wifi -j MASQUERADE")
		os.execute("iptables --append FORWARD --in-interface wifi -j ACCEPT")

		self.__share()

	def __share(self):
		os.execute("sysctl -w net.ipv4.ip_forward=1")