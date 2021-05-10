FROM python:3.6


WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    supervisor

COPY celery.conf /etc/supervisor/conf.d/celery.conf

RUN mkdir -p /var/log/celery

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]