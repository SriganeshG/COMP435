from scapy.all import *

sendp(Ether(src="01:02:03:04:05:06")/IP(dst="127.0.0.1"))
