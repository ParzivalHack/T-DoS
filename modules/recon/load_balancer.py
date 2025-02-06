from scapy.all import IP, TCP, sr1
import numpy as np
import requests
from typing import Dict, Any

class LoadBalancerDetector:
    def __init__(self, target: str):
        self.target = target
        
    def detect(self) -> Dict[str, Any]:
        """Detect load balancer using TTL variance and HTTP headers"""
        ttl_results = self._analyze_ttl_variance()
        header_results = self._check_http_headers()
        
        return {
            'ttl_variance': ttl_results,
            'http_headers': header_results,
            'load_balancer_detected': ttl_results['is_lb'] or header_results['is_lb']
        }

    def _analyze_ttl_variance(self) -> Dict[str, Any]:
        """Analyze TTL variance across multiple probes"""
        ttl_values = []
        for _ in range(30):  # Send 30 probes
            packet = IP(dst=self.target)/TCP(dport=80, flags="S")
            reply = sr1(packet, timeout=1, verbose=0)
            if reply:
                ttl_values.append(reply.ttl)
        
        if not ttl_values:
            return {'is_lb': False, 'variance': 0.0}
        
        variance = np.var(ttl_values)
        return {
            'is_lb': variance > 2.0,  # High variance indicates multiple paths
            'variance': round(variance, 2)
        }

    def _check_http_headers(self) -> Dict[str, Any]:
        """Check for load balancer headers"""
        try:
            response = requests.get(f"http://{self.target}", timeout=5)
            headers = response.headers
            
            lb_indicators = [
                'X-LB', 'X-LoadBalancer', 'X-Forwarded-For',
                'X-Forwarded-Proto', 'X-Real-IP'
            ]
            
            return {
                'is_lb': any(indicator in headers for indicator in lb_indicators),
                'headers': {k: v for k, v in headers.items() if k in lb_indicators}
            }
        except:
            return {'is_lb': False, 'headers': {}}