from django.urls import path
from .views import  (
  RNDCabinetsListAPI,
  KRDCabinetsListAPI,
  SCHCabinetsListAPI,
  KRDScheduleListAPI,
  RNDScheduleListAPI,
  SCHScheduleListAPI,
  CabinetsListAPI
  )

app_name = "skyreg"

urlpatterns = [

    path("cabinets/rostov", RNDCabinetsListAPI.as_view(), name="rndcabinets"),
    path("cabinets/sochi", SCHCabinetsListAPI.as_view(), name="schcabinets"),
    path("cabinets/krasnodar", KRDCabinetsListAPI.as_view(), name="krdcabinets"),
    path("schedule/krasnodar", KRDScheduleListAPI.as_view(), name="krdschedule"),
    path("schedule/rostov", RNDScheduleListAPI.as_view(), name="rndschedule"),
    path("schedule/sochi", SCHScheduleListAPI.as_view(), name="schschedule"),
    path("cabinets/list/", CabinetsListAPI.as_view(), name="cabinets" ),
]
