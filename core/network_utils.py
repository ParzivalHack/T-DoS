import random
import re
from ipaddress import ip_address, ip_network

def random_ip() -> str:
    """Generate random valid IP address"""
    return f"{random.randint(1,255)}.{random.randint(0,255)}." \
           f"{random.randint(0,255)}.{random.randint(0,255)}"

def is_cloudflare_ip(ip: str) -> bool:
    """Check if IP belongs to Cloudflare"""
    cf_ranges = [
        ip_network('173.245.48.0/20'),
        ip_network('103.21.244.0/22'),
        ip_network('104.16.0.0/13')
    ]
    try:
        return any(ip_address(ip) in network for network in cf_ranges)
    except ValueError:
        return False

def validate_port(port: int) -> bool:
    """Check if port is valid"""
    return 1 <= port <= 65535