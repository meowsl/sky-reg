from django.urls import path
from .views import (
  ApplicationsCreateAPIView,
  ApplicationsAPIView,
  ApplicationsUpdateAPIViev,
  KRDScheduleListAPI,
  RNDScheduleListAPI,
  SCHScheduleListAPI,
  CabinetsListAPI
  )


app_name = "personals"

urlpatterns = [
    path("applications/create/", ApplicationsCreateAPIView.as_view()),
    path("applications/list/", ApplicationsAPIView.as_view(), name="applications"),
    path("applications/update/<int:pk>", ApplicationsUpdateAPIViev.as_view(), name="update"),
    path("schedule/krasnodar", KRDScheduleListAPI.as_view(), name="krdschedule"),
    path("schedule/rostov", RNDScheduleListAPI.as_view(), name="rndschedule"),
    path("schedule/sochi", SCHScheduleListAPI.as_view(), name="schschedule"),
    path("cabinets/list/", CabinetsListAPI.as_view(), name="cabinets" ),
]
