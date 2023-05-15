#!/usr/bin/python3
# Script : OpsChallenge12.py
# Purpose: Scans an IP for a range of ports while randomizing the source port and ICMP Ping Sweep Mode
# Why    : Identifying potential open ports while trying to avoid detection and checking which hosts are up

from scapy.all import *
import random
import ipaddress
import logging
# Supresses a constant warning message
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def get_network_address():
    
    #Prompts the user for a network address with CIDR block and returns the network address and subnet mask.
    
    #Returns:
    #tuple: The network address and subnet mask as strings
   
    while True:
        try:
            network_address = input("Enter the network address with CIDR block such as 192.168.1.0/24): ")
            ipaddress.ip_network(network_address)
            return str(ipaddress.ip_network(network_address).network_address), str(ipaddress.ip_network(network_address).netmask)
        except ValueError:
            print("Invalid network address. Please try again.")

def ping_sweep(network_address):
    
    #Pings all hosts on the network except for the network address and broadcast address.
    #Prints the status of each host and returns the number of hosts that are online.
    
    #Parameters:
    #network_address (str): The network address to scan
    
    #Returns:
    #int: The number of hosts that are online

    network = ipaddress.ip_network(network_address)
    online_hosts = 0
    
    for host in network.hosts():
        if str(host) != str(network.network_address) and str(host) != str(network.broadcast_address):
            response = sr1(IP(dst=str(host))/ICMP(), timeout=0.5, verbose=0)
            if response is None:
                print(f"{host} is down or unresponsive.")
            elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
                print(f"{host} is actively blocking ICMP traffic.")
            else:
                print(f"{host} is responding.")
                online_hosts += 1
    
    return online_hosts

def tcp_port_range_scan(target_ip, port_range):
    
    #Scans a host IP for a range of TCP ports while randomizing the source port.
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

def user_menu():
    
    #Prompts the user for a choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode.
    #Calls the appropriate function based on the user's choice.
    
    while True:
        try:
            choice = int(input("Choose a mode:\n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\n3. Exit\n"))
            if choice == 1:
                target_ip = input("Enter the target IP address: ")
                port_range = range(int(input("Enter the starting port number: ")), int(input("Enter the ending port number: "))+1)
                tcp_port_range_scan(target_ip, port_range)
                break
            elif choice == 2:
                network_address, subnet_mask = get_network_address()
                print(f"Scanning network {network_address}/{subnet_mask}...")
                online_hosts = ping_sweep(f"{network_address}/{subnet_mask}")
                print(f"{online_hosts} hosts are online.")
                break
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

user_menu()
