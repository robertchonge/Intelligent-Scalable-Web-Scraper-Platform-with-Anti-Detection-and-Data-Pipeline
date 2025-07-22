proxies/proxy_manager.py

import random
import time
import logging

class ProxyManager:
    def __init__(self, proxies=None):
        self.proxies = proxies or []
        self.logger = logging.getLogger('ProxyManager')
        self.health = {p: True for p in self.proxies}

    def get_random_proxy(self):
        healthy_proxies = [p for p in self.proxies if self.health.get(p, False)]
        if not healthy_proxies:
            self.logger.warning("No healthy proxies available")
            return None
        proxy = random.choice(healthy_proxies)
        self.logger.info(f"Selected proxy: {proxy}")
        return proxy

    def mark_proxy_down(self, proxy):
        self.health[proxy] = False
        self.logger.warning(f"Marked proxy as down: {proxy}")

    def mark_proxy_up(self, proxy):
        self.health[proxy] = True
        self.logger.info(f"Marked proxy as up: {proxy}")

    def health_check(self):
        self.logger.info("Starting proxy health check")
        for proxy in self.proxies:
            # Simulate health check
            # Replace with real HTTP request to test proxy
            time.sleep(0.1)  # Simulate delay
            self.health[proxy] = True  # Assume all good for demo
        self.logger.info("Proxy health check complete")
