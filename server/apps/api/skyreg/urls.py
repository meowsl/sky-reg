from django.urls import path
from .views import ApplicationsAPIView, ApplicationsCreateAPIView

app_name = "skyreg"

urlpatterns = [
    path("applications/", ApplicationsAPIView.as_view(), name="applications"),
    path("applicationsCreate/", ApplicationsCreateAPIView.as_view(), name="applicationsCreate"),
]
