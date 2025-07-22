# Intelligent-Scalable-Web-Scraper-Platform-with-Anti-Detection-and-Data-Pipeline

## Overview
This project is a modular,scalable Python platform for scraping websites, designed to handle dynamic content, proxy rotation,asynchronous task processing and provide monitoring with Prometheus.

## Features
- Async scraping with aiohttp
- Celery task queue with Redis broker
- Proxy management and health checks
- Headless browser support via Playwright
- Prometheus metrics for monitoring
- REST API with token-based auth for device status
- Modular scrapers with base and site-specific implementations

## Setup
1. Install dependencies:

```bash
pip install -r requirements.txt
playwright install

2. Run Redis server locally or connect to remote.

3. Start Celery worker:

celery -A tasks.scrape_tasks worker --loglevel=info

4. Start Prometheus metrics server by importing and calling start_metrics_server() in your app.


5. Run API:

uvicorn api.rest:app --host 0.0.0.0 --port 8080

6. Submit scraping tasks as needed.

##Configuration

-Update config/settings.py for URLs, proxies, and tokens.

##License

@MIT License
Author:Robert Chonge
Email:robertchonge07@gmail.com
