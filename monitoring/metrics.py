from prometheus_client import start_http_server, Counter, Gauge
import logging

SCRAPE_SUCCESS = Counter('scraper_success_total', 'Total successful scrapes')
SCRAPE_FAILURE = Counter('scraper_failure_total', 'Total failed scrapes')
CURRENT_RUNNING = Gauge('scraper_running_tasks', 'Number of currently running scrape tasks')

def start_metrics_server(port=8000):
    """
    Start Prometheus metrics HTTP server on given port.
    Call this early on app startup.
    """
    start_http_server(port)
    logging.info(f"Prometheus metrics server started on port {port}")
