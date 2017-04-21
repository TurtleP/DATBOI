'''
Packet sniffer in python using the pcapy python library
 
Project website
http://oss.coresecurity.com/projects/pcapy.html
'''
 
import socket
from struct import *
import datetime
import pcapy
import sys
 
cap = pcapy.open_live("DATBOI", 65536, 1 , 0)

# IP 6	:	TCP (HTTP(S))
# IP 17	:	UDP

def addr(a):
	return '{:02X}:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}'.format(a[0], a[1], a[2], a[3], a[4], a[5])

def parse(pack):
	eth_length = 14
	eth_header = pack[:eth_length]
	eth_struct = unpack('!6s6sH', eth_header)
	eth_protoc = socket.ntohs(eth_struct[2])

	print("Dest: " + addr(packet[0:6]) + " Source: " + addr(packet[6:12]) + " Protocol: " + str(eth_protoc))
	if eth_protoc == 8:
		ip_header_bytes = packet[eth_length:20 + eth_length]
		ip_header = unpack('!BBHHHBBH4s4s', ip_header_bytes)

		version = ip_header[0] >> 4

		ip_protocol = ip_header[6]

		ip_header_length = ip_header[0] & 0xF * 4

		print("IP Protocol: " + str(protocol) + " v" + str(version) + " length: " + str(ip_header_length)) 

		if ip_protocol == 6:
			tcp = ip_header_length + eth_length
			tcp_header_bytes = packet[t:t+20]

			tcp_header = unpack('!HHLLBBHHH', tcp_header_bytes)

			if tcp_header[0] == 443: # HTTP
				print("Destination port: " + str(tcp_header[1] + " Sequence: " + str(tcp_header[2]) + " Acknowledge: " + tcp_header[3])

#start sniffing packets
while(1) :
	(header, packet) = cap.next()
	parse(packet)