from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class SiteAScraper(BaseScraper):
    async def parse(self, html):
        # Example: parse title and first h1 text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No title'
        h1 = soup.find('h1')
        heading = h1.get_text(strip=True) if h1 else 'No H1 found'
        return {
            'url': self.url,
            'title': title,
            'heading': heading
        }
