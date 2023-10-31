from django.urls import path
from .views import  ApplicationsAPIView, ApplicationsCreateAPIView, CabinetsAPIView

app_name = "skyreg"

urlpatterns = [
    path("applications-create/", ApplicationsCreateAPIView.as_view(), name="applicationsCreate"),
    path("applications/", ApplicationsAPIView.as_view(), name="applications"),
    path("cabinets/", CabinetsAPIView.as_view(), name="cabinets")
]
