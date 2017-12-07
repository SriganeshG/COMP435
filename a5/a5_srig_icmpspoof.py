from scapy.all import *
send(IP(src="152.2.254.254",dst="8.8.8.8")/ICMP())
