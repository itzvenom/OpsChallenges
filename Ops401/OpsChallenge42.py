#!/usr/bin/python3

# Script : OpsChallenge42.py - Attack Tools Part 2 of 3
# Purpose: A tool to easily execute various Nmap scans and display results.
# Why    : Automate repetitive Nmap scans to simplify the security scanning workflow.

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Agressive Scan""") ### TODO: Select what your third scan type will be
print("You have selected option: ", resp)

range = input("Choose which port range do you wish to scan:")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-T4 -A -v')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    for host in scanner.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, scanner[host].hostname()))
     print('State : %s' % scanner[host].state())
     for proto in scanner[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)

         lport = scanner[host][proto].keys()
         for port in lport:
             print ('port : %s\tstate : %s\tproduct: %s\tversion: %s\textrainfo: %s\tname: %s' % (port, scanner[host][proto][port]['state'], scanner[host][proto][port]['product'], scanner[host][proto][port]['version'], scanner[host][proto][port]['extrainfo'], scanner[host][proto][port]['name']))
elif resp >= '4':
    print("Please enter a valid option")
