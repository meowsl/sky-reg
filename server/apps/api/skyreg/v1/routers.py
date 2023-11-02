from django.urls import path
from .views import  RNDCabinetsAPIView, KRDCabinetsAPIView, SCHCabinetsAPIView

app_name = "skyreg"

urlpatterns = [

    path("rostov-cabinets/", RNDCabinetsAPIView.as_view(), name="rndcabinets"),
    path("sochi-cabinets/", SCHCabinetsAPIView.as_view(), name="schcabinets"),
    path("krasnodar-cabinets/", KRDCabinetsAPIView.as_view(), name="krdcabinets"),
]
