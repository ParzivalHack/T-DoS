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
* pip install python2
* pip install git
* pip install scapy (if you have Python 3 or more, even if you already installed scapy, execute this command: ```python2 -m pip install scapy[basic]```)
* git clone https://github.com/ParzivalHack/T-DoS

# Usage
Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws. Use this tool only on your own network or on networks from which you have obtained permission. The creator of this tool, CANNOT be held liable for any misuse of it.
* cd T-DoS
* python2 T-DoS.py

# Update
* cd T-DoS
* bash update.sh

# Screenshots
![image](https://user-images.githubusercontent.com/82817793/208091289-086d337e-f3a4-4d2f-9c15-749e74dab156.png)


# License
This tool is under the MIT License.

# Special Thanks
* Thanks to  <a href = "https://github.com/EpicBen146" > EpicBen146 </a> for helping me test T-DoS.
* Thanks to  <a href = "https://github.com/alsacchi" > Andrea Sacchi </a> for fixing all the bugs i couldn't fix by myself.
