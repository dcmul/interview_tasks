from celery import shared_task
import time
import datetime
from solution.main.models import SmartMeter, MeterReading

@shared_task
def save_meter_reading(meter_id, meter_date, meter_reading):
    print('=Item called=')
    print(meter_id, meter_date, meter_reading)
    MeterReading.save_reading(meter_id, meter_date, meter_reading)
    return True
