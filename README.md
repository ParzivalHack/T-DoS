# What's a DoS/DDoS attack?
Distributed Denial Of Service (DDoS) attacks are a subclass of denial of service (DoS) attacks. A DDoS attack involves multiple connected online devices, collectively known as a botnet, which are used to overwhelm a target website with fake traffic.

As you can see from the image below, there are 14 different types of DoS/DDoS attacks; the tool i developed, T-DoS, is able to do TCP SYN Flood Attack (Number 3), HTTP Flood (Number 6), Slowloris Ping Attack (Number 14), Ping Flood Attack and Ping Of Death (Number 13).

![image](https://user-images.githubusercontent.com/82817793/205066388-55fb2697-e1f6-4214-8b5f-1d903bd61567.png)

P.s. my goal is to slowly add, to T-DoS, all 14 types of attacks.

# What's T-DoS?
T-DoS is a Multi-Purpose DoS Tool,written in Python 2, right now capable of doing "only" 5 out of 14 types of DoS Attacks. It's meant to be used for Pentesting, but can also be used for testing of your own network (like your own router, website or webserver) and researching. It has an easy-to-use cli wizard interface, perfect for beginners, and right now it works on Termux, Kali Linux and ParrotOS.
![image](https://user-images.githubusercontent.com/82817793/206921534-66416fe9-c8a0-4b9f-93c2-e40988de7157.png)


# Installation of T-DoS
* apt update && apt upgrade
* pip install python
* pip install python2
* pip install git
* pip install scapy
* git clone https://github.com/ParzivalHack/T-DoS

# Usage
Disclaimer: Illecit use of this tool could lead to a violation of federal and local laws. Use this tool only on your own network or on networks from which you have obtained permission. The creator of this tool, CANNOT be held liable for any misuse of it.
* cd T-DoS
* python2 T-DoS.py
![image](https://user-images.githubusercontent.com/82817793/205044426-c1189d3c-ada5-4800-9be6-775a2bbbf3a9.png)


# Update
* cd T-DoS
* bash update.sh

# License
This tool is under the MIT License.
