from scapy.all import *
A = '152.2.254.254' # spoofed source IP address
B = '127.0.0.1' # destination IP address
payload = "the god sri o.g."
spoofed_packet = IP(src=A, dst=B) / payload
send(spoofed_packet)
