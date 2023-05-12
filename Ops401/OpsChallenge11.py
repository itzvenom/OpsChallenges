#!/usr/bin/python3

# Script : OpsChallenge11.py
# Purpose: Scans a host IP for a range of ports while randomizing the source port
# Why    : Identifying potential open ports while trying to avoid detection

from scapy.all import *
import random

# Define target IP address and port range
target_ip = "192.168.0.1"
port_range = range(1, 10)

# Define the function to scan a single port
def scan_port(port):
    # Create SYN packet
    packet = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535), dport=port, flags="S")

    # Send packet and capture response
    response = sr1(packet, timeout=1, verbose=0)

    # Check if response is received
    if response is None:
        print("Port",port,"is either filtered or closed")
    
    elif(response.haslayer(TCP)):
        if(response.getlayer(TCP).flags == 0x12):
            send_rst = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535),dport=port,flags="R")
            send(send_rst)
            print("Port",port,"is open")
            
        elif(response.getlayer(TCP).flags == 0x14):      
            print("Port",port,"is closed")

# Scan each port in the specified range
for port in port_range:
    scan_port(port)
