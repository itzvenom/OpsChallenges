#!/usr/bin/python3

# Script : OpsChallenge26.py
# Purpose: Scans a host IP for a range of ports while randomizing the source port with logging to port_scan.log.
# Why    : Identifying potential open ports while trying to avoid detection

import logging
from scapy.all import *
import random

# Set up logging
logging.basicConfig(filename='port_scan.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

# Define target IP address and port range
target_ip = "8.8.8.8"
port_range = range(1, 65535)

# Define the function to scan a single port
def scan_port(port):
    # Create SYN packet
    packet = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535), dport=port, flags="S")

    # Send packet and capture response
    response = sr1(packet, timeout=1, verbose=0)

    try:
        # Check if response is received
        if response is None:
            logging.warning("Port %s is either filtered or closed", port)
    
        elif(response.haslayer(TCP)):
            if(response.getlayer(TCP).flags == 0x12):
                send_rst = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535),dport=port,flags="R")
                send(send_rst)
                logging.info("Port %s is open", port)
                
            elif(response.getlayer(TCP).flags == 0x14):
                logging.warning("Port %s is closed", port)
    
    except Exception as e:
        logging.error("Error while scanning port %s: %s", port, e)

# Scan each port in the specified range
for port in port_range:
    scan_port(port)
