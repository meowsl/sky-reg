from django.urls import path
from .views import ApplicationsCreateAPIView, ApplicationsAPIView

app_name = "personals"

urlpatterns = [
    path("applications/create/", ApplicationsCreateAPIView.as_view()),
    path("applications/list/", ApplicationsAPIView.as_view(), name="applications"),
]
