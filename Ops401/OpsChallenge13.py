#!/usr/bin/python3
# Script : OpsChallenge12.py
# Purpose: Check if target IP is up, if it is prompt for port number and scan the target.
# Why    : Identifying potential open ports.

from scapy.all import *
import random
import ipaddress
import logging
# Supresses a constant warning message
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def ping_sweep(target_ip):
    
    #Pings the target IP. 
    #Prints the status of the host and returns True if host is online.
    
    #Parameters:
    #target_ip (str): The IP address of the target host
    
    #Returns:
    #True if target host is online, False otherwise
    response = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)
    if response is None:
        print(f"{target_ip} is down or unresponsive.")
        return False
    elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
        print(f"{target_ip} is actively blocking ICMP traffic.")
        return False 
    else:
        print(f"{target_ip} is responsive.")
        return True 

def tcp_port_range_scan(target_ip, port_range):
    
    #Scans a host IP.
    #Prints the status of each port.
    
    #Parameters:
    #target_ip (str): The IP address of the target host
    #port_range (range): The range of TCP ports to scan
    
    for port in port_range:
        # Create SYN packet
        packet = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535), dport=port, flags="S")
        
        # Send packet and capture response
        response = srp1(packet, timeout=1, verbose=0)
        
        # Check if response is received
        if response is None:
            print(f"Port {port} is either filtered or closed.")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                send_rst = IP(dst=target_ip)/TCP(sport=random.randint(1024, 65535),dport=port,flags="R")
                send(send_rst)
                print(f"Port {port} is open.")
            elif response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed.")

# Continuosly ask for a valid IP address.
while True:
    try: 
        target_ip = input("Enter the target IP address: ")
        ip = ipaddress.ip_address(target_ip)
        break
    except ValueError:
        print("Invalid IP address. Please try again.")

# Check if host is responsive to ICMP
host_is_up = ping_sweep(target_ip) 

# If host is up ask for port to be scanned and call tcp_port_range_scan function.
if host_is_up:
    
    while True:
        try: 
            start_port = int(input("Enter the starting port number: "))
            end_port = int(input("Enter the ending port number: "))
            if start_port < 0 or end_port < 0 or start_port > end_port or end_port > 65535:
                print("Invalid port range. Start port must be less than end port and both must be greater than 0. End port must be lower than 65535.")
                continue
            port_range = range(start_port, end_port+1)
            break
        except ValueError:
            print("Invalid port range. Port numbers must be integers.")
    
    tcp_port_range_scan(target_ip, port_range) 
