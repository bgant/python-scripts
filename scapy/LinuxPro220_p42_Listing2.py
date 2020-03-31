# Step 1: Imports
from scapy.all import *
from prettytable import PrettyTable
from collections import Counter

# Step 2: Read and Append
packets = rdpcap("example.pcap")
srcIP = []
for packet in packets:
    if IP in packet:
        try:
            srcIP.append(packet[IP].src)
        except:
            pass

# Step 3: Count
count = Counter()
for ip in srcIP:
    count[ip] += 1

# Step 4: Table and Print
table = PrettyTable(["IP", "Count"])
for ip, count in count.most_common():
    table.add_row([ip, count])
print(table)
