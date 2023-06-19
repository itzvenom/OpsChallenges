#!/bin/python

# Script         Ops Challenge: Event Logging Tool Part 1 of 3
# Purpose        Proceeds to ping 8.8.8.8 indefinitely while printing a timestamp and success or failure message to the console and writing it to a log file.
# Why            Learn how to use the logging library.

import os
import time
import logging

# Configure logging settings
logging.basicConfig(filename="ping_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

destination_ip = "8.8.8.8"
status = ""

logging.info('Starting script... Pinging 8.8.8.8\n')

def ping(destination_ip):
    response = os.system(f"ping -c 1 {destination_ip} > ping_log.txt 2>&1")
    if response == 0:
        status = "success"
    else:
        status = "failure"

    log_entry = f"Network {status} to {destination_ip}"
    logging.info(log_entry)

# Main loop
while True:
    try:
        ping(destination_ip)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    time.sleep(2)
