<a href='https://github.com/ParzivalHack/T-DoS'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Git-Clones&query=count&url=https://gist.githubusercontent.com/ParzivalHack/T-DoS&logo=github'></a>
# What's a DoS/DDoS attack?
Distributed Denial Of Service (DDoS) attacks are a subclass of denial of service (DoS) attacks. A DDoS attack involves multiple connected online devices, collectively known as a botnet, which are used to overwhelm a target website with fake traffic.

As you can see from the image below, there are 14 different types of DoS/DDoS attacks; the tool i developed, T-DoS, is able to do TCP SYN Flood Attack (Number 3), HTTP Flood (Number 6), Slowloris Ping Attack (Number 14), Ping Flood Attack, Ping Of Death Attack (Number 13), ICMP Flood Attack (Number 2) and IP Fragmentation Flood (Number 5).

![image](https://user-images.githubusercontent.com/82817793/205066388-55fb2697-e1f6-4214-8b5f-1d903bd61567.png)

P.s. my goal is to slowly add, to T-DoS, all 14 types of attacks.

# What's T-DoS?
T-DoS is a Multi-Purpose DoS Tool, written in Python 3, right now capable of doing "only" 7 out of 14 types of DoS Attacks. It's meant to be used for Pentesting, but can also be used for testing of your own network (like your own router, website or webserver) and researching. It has an easy-to-use cli wizard interface, perfect for beginners, and right now it works on Termux, Kali Linux and ParrotOS.

![image](https://user-images.githubusercontent.com/82817793/208090844-f0ce76cf-0391-486b-8fb3-f73dee905a34.png)

# Installation of T-DoS
* apt update && apt upgrade
* pip install python
* pip install git
* pip install scapy
* git clone https://github.com/ParzivalHack/T-DoS

# Usage
Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws. Use this tool only on your own network or on networks from which you have obtained permission. The creator of this tool, CANNOT be held liable for any misuse of it.
* cd T-DoS
* python T-DoS.py

# Update
* cd T-DoS
* bash update.sh

# Screenshots
## SYN Flood:
![image](https://user-images.githubusercontent.com/82817793/208093713-22862d80-b536-410a-9408-b71be2738449.png)


## HTTP Flood:
![image](https://user-images.githubusercontent.com/82817793/208091769-748a2b25-a6d6-459a-8f4d-1cf38b243395.png)

## Slowloris Ping:
![image](https://user-images.githubusercontent.com/82817793/208422926-9db17aad-02c4-4989-b68c-7d48d9b11003.png)

## Ping Flood:
![image](https://user-images.githubusercontent.com/82817793/208091997-c28d9301-c007-48e4-afc2-62f1ad9aed57.png)
## Ping of Death:
![image](https://user-images.githubusercontent.com/82817793/208092416-756145a5-28df-4cc2-9981-79cf72fc7294.png)

## ICMP Flood:
![image](https://user-images.githubusercontent.com/82817793/208092684-d4c95f63-fd75-4e61-aafb-d59ff628be7f.png)

## IP Fragmentation Flood:
![image](https://user-images.githubusercontent.com/82817793/208092803-9e455cba-766e-4e92-a513-7c283ffb1ddd.png)


# License
This tool is under the MIT License.

# Special Thanks
* Thanks to  <a href = "https://github.com/EpicBen146" > EpicBen146 </a> for helping me test T-DoS.
* Thanks to  <a href = "https://github.com/alsacchi" > Andrea Sacchi </a> for fixing all the bugs i couldn't fix by myself.
