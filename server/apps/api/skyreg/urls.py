from django.urls import path
from .views import ApplicationsAPIView, ApplicationsCreateAPIView, CabinetsAPIView

app_name = "skyreg"

urlpatterns = [
    path("applications/", ApplicationsAPIView.as_view(), name="applications"),
    path("applicationsCreate/", ApplicationsCreateAPIView.as_view(), name="applicationsCreate"),
    path("cabinet/", CabinetsAPIView.as_view(), name="cabinets")
]
