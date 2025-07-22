import os

# Redis and Celery
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
BROKER_URL = REDIS_URL

# Proxy list
PROXIES = [
    'http://proxy1.example.com:3128',
    'http://proxy2.example.com:3128',
]

# URLs to scrape
SCRAPE_TARGETS = [
    'https://example.com',
    'https://httpbin.org/html',
]

# API token for REST endpoints
API_TOKEN = os.getenv('API_TOKEN', 'secret-token')

# Logging config can be added here or via logging.conf file
