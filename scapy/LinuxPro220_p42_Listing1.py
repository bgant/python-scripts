# Source: Linux Pro Magazine Issue 220 (March 2019) Page 42

# Step 1: Import scapy
from scapy.all import *

# Step 2: Read the PCAP using rdpcap
packets = rdpcap("example.pcap")

# Step 3: Loop and print an IP in a packet in Scapy by looking at Layer 2
for packet in packets:
    if IP in packet:
        try:
            print(packet[IP].src)  # Source IP
        except:
            pass  # Do not faile with an error if no IP in packet

