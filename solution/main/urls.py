from django.urls import path, include
from . import views


urlpatterns = [
    path("<str:meterid>/<str:startdate>_<str:starttime>/<str:enddate>_<str:endtime>", views.QueryMeterView.as_view(), name='trans_list' ),
]