import sys
import yaml
import asyncio
from datetime import datetime
from typing import List

class EthicalEnforcer:
    def __init__(self):
        self.config = self._load_config()
        self.whitelist = self._load_whitelist()
        self.start_time = datetime.now()
        self.packet_count = 0
        
    def _load_config(self) -> dict:
        try:
            with open('config/config.yaml') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("❌ Missing config file! Using defaults")
            return {
                'max_duration': 300,
                'rate_limit': 1000
            }
            
    def _load_whitelist(self) -> List[str]:
        try:
            with open(self.config.get('whitelist_path', 'config/whitelist.txt')) as f:
                return [line.strip() for line in f if not line.startswith('#')]
        except FileNotFoundError:
            print("❌ Critical: Missing whitelist file!")
            sys.exit(1)

    def validate_target(self, target: str) -> bool:
        """Check if target is in whitelist"""
        if not any(target in entry or entry.endswith('*') and target.startswith(entry[:-1]) for entry in self.whitelist):
            print(f"🚫 Unauthorized target: {target}")
            sys.exit(1)
        return True
            
    def check_rate_limit(self, current_rate: float) -> bool:
        """Enforce rate limiting"""
        max_rate = self.config.get('rate_limit', 1000)
        if current_rate > max_rate:
            print(f"⚠️ Rate limit exceeded ({max_rate} packets/s)")
            return False
            
        max_duration = self.config.get('max_duration', 300)
        elapsed = (datetime.now() - self.start_time).seconds
        if elapsed > max_duration:
            print(f"⏳ Max duration exceeded ({max_duration}s)")
            return False
            
        return True

    def kill_switch(self):
        """Emergency shutdown procedure"""
        print("\n🔴 Ethical kill switch activated!")
        sys.exit(0)