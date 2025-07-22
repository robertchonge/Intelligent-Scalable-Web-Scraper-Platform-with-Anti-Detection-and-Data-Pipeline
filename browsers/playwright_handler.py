import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import logging

logger = logging.getLogger('playwright_handler')

async def fetch_dynamic_content(url: str, timeout=15000) -> str | None:
    """
    Using Playwright to load dynamic pages (JS-heavy),
    return page content as string.
    """
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, timeout=timeout)
            await page.wait_for_load_state('networkidle', timeout=timeout)
            content = await page.content()
            await browser.close()
            logger.info(f"Successfully fetched dynamic content: {url}")
            return content
    except PlaywrightTimeoutError:
        logger.error(f"Timeout loading page: {url}")
    except Exception as e:
        logger.error(f"Playwright error for {url}: {e}")
    return None
