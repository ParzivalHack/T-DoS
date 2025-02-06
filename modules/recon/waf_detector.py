import requests
from core.network_utils import is_cloudflare_ip

class WAFDetector:
    def __init__(self, target):
        self.target = target
        
    def detect(self):
        tests = [
            self._check_cloudflare,
            self._check_aws_waf,
            self._check_generic
        ]
        
        for test in tests:
            if result := test():
                return result
        return "No WAF Detected"

    def _check_cloudflare(self):
        if is_cloudflare_ip(self.target):
            return "Cloudflare"
        return False

    def _check_aws_waf(self):
        resp = requests.get(f"http://{self.target}")
        if 'x-amz-cf-id' in resp.headers:
            return "AWS WAF"
        return False

    def _check_generic(self):
        try:
            resp = requests.get(f"http://{self.target}/?=<script>alert(1)</script>")
            if resp.status_code == 403:
                return "Generic WAF (403 Forbidden)"
        except:
            pass
        return False