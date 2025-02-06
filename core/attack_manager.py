import asyncio
from dataclasses import dataclass
from typing import Callable, Any
from core.ethical_check import EthicalEnforcer

@dataclass
class AttackConfig:
    target: str
    port: int
    duration: int = 0  # 0 = manual stop
    packets: int = 0   # 0 = unlimited
    threads: int = 50
    rate_limit: int = 1000

class AttackManager:
    def __init__(self):
        self.eth = EthicalEnforcer()
        self.active_attacks = set()
        
    async def _attack_wrapper(self, attack_func: Callable, config: AttackConfig):
        """Wrapper for ethical enforcement"""
        self.eth.validate_target(config.target)
        start_time = asyncio.get_event_loop().time()
        packets_sent = 0
        
        while True:
            if config.packets > 0 and packets_sent >= config.packets:
                break
            if config.duration > 0 and (asyncio.get_event_loop().time() - start_time) >= config.duration:
                break
            if not self.eth.check_rate_limit(packets_sent/config.duration if config.duration > 0 else 0):
                await asyncio.sleep(1)
                continue
                
            await attack_func(config)
            packets_sent += 1
            
    async def launch_attack(self, attack_func: Callable, config: AttackConfig):
        tasks = []
        for _ in range(config.threads):
            task = asyncio.create_task(self._attack_wrapper(attack_func, config))
            tasks.append(task)
        
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            self.eth.kill_switch()