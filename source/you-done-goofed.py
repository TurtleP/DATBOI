# this is the 'you done goofed with ARP spoofs n stuff' file

import sys
import netifaces
from scapy.all import *

victim_ip, victim_mac, gateway_ip, gateway_mac = str(sys.argv[1]), str(sys.argv[2]), netifaces.gateways()['default'][netifaces.AF_INET][0][0], str(sys.argv[3])

print(victim_ip, victim_mac, gateway_ip, gateway_mac)

def restore(victim_ip, victim_mac, gateway_ip, gateway_mac):
	# Send the victim an ARP packet pairing 
	#the gateway ip with the correct mac address
	packet = ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=victim_ip, hwdst=victim_mac)
	send(packet, verbose=0)

restore(victim_ip, victim_mac, gateway_ip, gateway_mac)