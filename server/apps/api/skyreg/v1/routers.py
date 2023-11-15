from django.urls import path
from .views import  (
  KRDScheduleListAPI,
  RNDScheduleListAPI,
  SCHScheduleListAPI,
  CabinetsListAPI
  )

app_name = "skyreg"

urlpatterns = [
    path("schedule/krasnodar", KRDScheduleListAPI.as_view(), name="krdschedule"),
    path("schedule/rostov", RNDScheduleListAPI.as_view(), name="rndschedule"),
    path("schedule/sochi", SCHScheduleListAPI.as_view(), name="schschedule"),
    path("cabinets/list/", CabinetsListAPI.as_view(), name="cabinets" ),
]
