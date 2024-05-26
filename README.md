This is simple job queue implementation for compute intensive tasks. 

It uses the following components:
 - fastapi for the web framework,
 - Celery with RabbitMQ for the distributed task queue,
 - Flower for real-time monitoring of Celery
 - Prometheus as the time-series database to store metrics scrapped from Flower
 - Graphana for visualing flower metrics from Prometheus

type docker-compose [start|restart] at root to start/restart all the containers

Follow this Flower documentation to setup flower-prometheus-graphana integration
- https://flower.readthedocs.io/en/latest/prometheus-integration.html

Monitoring:
 - http://localhost:8000/docs for Fastapi endpoints
 - http://localhost:5555 for Flower dashboard
 - http://localhost:9090 for Prometheus UI
 - http://localhost:3000 for Graphana dashboard

