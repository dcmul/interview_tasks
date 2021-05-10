from django.shortcuts import render

from rest_framework.views import APIView
import time
import secrets
from solution.main.models import SmartMeter, MeterReading

from . import views

from rest_framework.response import Response



class QueryMeterView(APIView):
    """
    List all Chats, or create a new chat.
    """
    authentication_classes = ()
    permission_classes = ()
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)    

    def get(self, request, format=None, *args, **kwargs):

        # densite, new_id = self.get_or_create_densite(request)

        # customer = kwargs['customer']
        # print(kwargs)
        meterid = kwargs['meterid']
        starttime = kwargs['starttime']
        endtime = kwargs['endtime']


        result = MeterReading.objects.filter(meter__account_no=meterid).values()[:100]

        response =  Response({'status':'success', 'data':result})
        # serializer = ChatSerializer(chat)
        return response