from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.
class SmartMeter(models.Model):
    account_no = models.CharField(max_length=36, unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'meter:%s' % (self.account_no, )

 
class MeterReading(models.Model):
    meter = models.ForeignKey(SmartMeter, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(null=True)
    energy_kwh = models.FloatField(null=True, default=0.0)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def save_reading(cls, meter_id, meter_date, meter_reading):
        meter, created = SmartMeter.objects.get_or_create(account_no=meter_id)
        reading = cls.objects.create(
            meter = meter,
            time_stamp = meter_date, 
            energy_kwh = meter_reading

            )

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

