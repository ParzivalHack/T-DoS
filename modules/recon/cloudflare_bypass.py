import dns.resolver
import requests
import re
from typing import List, Optional
from core.network_utils import is_cloudflare_ip

class CloudflareBypass:
    def __init__(self, domain: str):
        self.domain = domain
        
    def find_origin_ips(self) -> List[str]:
        """Find potential origin servers behind Cloudflare"""
        methods = [
            self._check_dns_history,
            self._check_subdomains,
            self._check_ssl_certs,
            self._check_old_records
        ]
        
        found_ips = []
        for method in methods:
            found_ips.extend(method())
            
        return list(set(ip for ip in found_ips if not is_cloudflare_ip(ip)))

    def _check_subdomains(self) -> List[str]:
        """Check common infrastructure subdomains"""
        subdomains = [
            'origin', 'direct', 'backend',
            'internal', 'server', 'prod'
        ]
        ips = []
        
        for sub in subdomains:
            try:
                answers = dns.resolver.resolve(f'{sub}.{self.domain}', 'A')
                ips.extend(str(rdata) for rdata in answers)
            except dns.resolver.NXDOMAIN:
                continue
        return ips

    def _check_ssl_certs(self) -> List[str]:
        """Check certificate transparency logs"""
        try:
            response = requests.get(
                f"https://crt.sh/?q=%.{self.domain}&output=json",
                timeout=10
            )
            return list(set(
                cert['common_name'] for cert in response.json()
                if re.match(r'^\d+\.\d+\.\d+\.\d+$', cert['common_name'])
            ))
        except:
            return []

    def _check_old_records(self) -> List[str]:
        """Check historical DNS records"""
        try:
            response = requests.get(
                f"https://securitytrails.com/domain/{self.domain}/dns",
                headers={'APIKEY': 'YOUR_API_KEY'},  # Add actual API key
                timeout=10
            )
            return re.findall(r'\d+\.\d+\.\d+\.\d+', response.text)
        except:
            return []