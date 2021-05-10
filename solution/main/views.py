from django.shortcuts import render

from rest_framework.views import APIView
import time
import secrets
from solution.main.models import SmartMeter, MeterReading
from dateutil.parser import parse

from . import views

from rest_framework.response import Response

def create_date(s):
    """
    Convert string to date. Return False is date is invalid.
    """
    try:
        return parse(s)
    except Exception:
        return False       

class QueryMeterView(APIView):
    """
    Disabling authentication for now.
    """
    authentication_classes = ()
    permission_classes = ()
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)    

    def get(self, request, format=None, *args, **kwargs):

        meterid = kwargs['meterid']
        starttime = kwargs['startdate']
        endtime = kwargs['enddate']
        starttime = kwargs['starttime']
        endtime = kwargs['endtime']


        start_string = '%s %s' % (kwargs['startdate'], kwargs['starttime'])
        date_start = create_date(start_string)
        if not date_start:
            return Response({'success':False, 'msg':'Invalid start String'}, status=400)


        end_string = '%s %s' % (kwargs['enddate'], kwargs['endtime'])         
        date_end = create_date(end_string)
        if not date_end:
            return Response({'success':False, 'msg':'Invalid End String'}, status=400)        
        # print(date_start, date_end)

        date_diffe = date_end - date_start

        if date_diffe.seconds > 60*60:
            return Response({'success':False, 'msg':'Difference between Start time and End Time should be less than one hour'}, status=400)

        result = MeterReading.objects.filter(
            meter__account_no=meterid,
            time_stamp__range = (date_start, date_end),
            ).values()[:100]

        response =  Response({'success':True, 'data':result}, status=200)
        
        return response