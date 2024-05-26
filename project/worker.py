from celery import Celery
import os
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load broker and backend URLs from environment variables
broker_url = os.environ.get('CELERY_BROKER_URL', 'amqp://guest:guest@rabbitmq:5672//')
backend_url = os.environ.get('CELERY_BACKEND_URL', 'rpc://')

celery_app = Celery('worker', broker=broker_url, backend=backend_url)

@celery_app.task
def do_work(payload):
    try:
        logging.info(f'Starting task with payload: {payload}')
        # Perform your task logic here
        time.sleep(30)
        logging.info(f'Task completed with payload: {payload}')
        return {"message": payload}
    except Exception as e:
        logging.error(f'Error occurred during task execution: {e}')
        return {"error": str(e)}