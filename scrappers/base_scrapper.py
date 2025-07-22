import logging
from abc import ABC, abstractmethod
import aiohttp
import asyncio

class BaseScraper(ABC):
    def __init__(self, url):
        self.url = url
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def parse(self, html):
        """Parse page content and extract data"""
        pass

    async def fetch(self, session):
        try:
            async with session.get(self.url, timeout=10) as response:
                response.raise_for_status()
                self.logger.info(f"Fetched URL: {self.url} Status: {response.status}")
                return await response.text()
        except Exception as e:
            self.logger.error(f"Fetch error for {self.url}: {e}")
            return None

    async def scrape(self, session):
        html = await self.fetch(session)
        if html:
            data = await self.parse(html)
            return data
        self.logger.warning(f"No data scraped from {self.url}")
        return None
