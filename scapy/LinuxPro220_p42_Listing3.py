# Step 1: Imports
from scapy.all import *
from prettytable import PrettyTable
from collections import Counter
import plotly

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
cnt = Counter()
for ip in srcIP:
    cnt[ip] += 1

# Step 4: Add Lists
xData = []
yData = []

for ip, count in cnt.most_common():
    xData.append(ip)
    yData.append(count)

# Step 5: Plot
plotly.offline.plot({"data":[plotly.graph_objs.Bar(x=xData, y=yData)]})

