#!/bin/python


#Script         Ops Challenge: Class 11 - Psutil
#Purpose        Create a Python file capable of using Psutil to fetch system information.
#Why            Learn how to use Psutil library to fetch system information.

# Import psutil library
import psutil

# Get CPU times
cpu_times = psutil.cpu_times()

# Open file for writing
with open('cpu_times.txt', 'w') as file:
    # Write CPU times to file
    file.write("Time spent by normal processes executing in user mode: " + str(cpu_times.user) + "seconds \n")
    file.write("Time spent by processes executing in kernel mode: " + str(cpu_times.system) + "seconds \n")
    file.write("Time when system was idle: " + str(cpu_times.idle) + "seconds \n")
    file.write("Time spent by priority processes executing in user mode: " + str(cpu_times.nice) + "seconds \n")
    file.write("Time spent waiting for I/O to complete: " + str(cpu_times.iowait) + "seconds\n")
    file.write("Time spent for servicing hardware interrupts: " + str(cpu_times.irq) + "seconds \n")
    file.write("Time spent for servicing software interrupts: " + str(cpu_times.softirq) + "seconds \n")
    file.write("Time spent by other operating systems running in a virtualized environment: " + str(cpu_times.steal) + "seconds \n")
    file.write("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: " + str(cpu_times.guest) + "seconds \n")