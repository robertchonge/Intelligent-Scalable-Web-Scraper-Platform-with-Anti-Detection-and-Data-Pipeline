from celery import Celery
import asyncio
import aiohttp
from scrapers.site_a_scraper import SiteAScraper
from data_pipeline.extractor import process_data
import logging

celery_app = Celery('tasks', broker='redis://localhost:6379/0')
logger = logging.getLogger('scrape_tasks')

@celery_app.task(bind=True, max_retries=3)
def scrape_site_a(self, url):
    try:
        asyncio.run(_async_scrape(url))
    except Exception as exc:
        logger.error(f"Task failed for {url}: {exc}")
        raise self.retry(exc=exc, countdown=10)

async def _async_scrape(url):
    async with aiohttp.ClientSession() as session:
        scraper = SiteAScraper(url)
        data = await scraper.scrape(session)
        if data:
            process_data(data)
        else:
            raise ValueError(f"No data scraped for {url}")
