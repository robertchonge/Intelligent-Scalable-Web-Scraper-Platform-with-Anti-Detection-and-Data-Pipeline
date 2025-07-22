from celery import Celery
import config.settings as settings

celery_app = Celery('webscraper', broker=settings.BROKER_URL)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

if __name__ == '__main__':
    celery_app.start()

