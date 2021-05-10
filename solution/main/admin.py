from django.contrib import admin
from solution.main.models import SmartMeter, MeterReading

# Register your models here.
@admin.register(SmartMeter)
class SmartMeterAdmin(admin.ModelAdmin):
    
    list_display = ('account_no', 'created')

@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    
    list_display = ('energy_kwh', 'time_stamp', 'meter',  )
