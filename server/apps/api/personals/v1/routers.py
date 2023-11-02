from django.urls import path
from .views import ApplicationsAPIView, ApplicationsCreateAPIView, PatientsCardsAPIView

app_name = "personals"

urlpatterns = [
    path("applications-create/", ApplicationsCreateAPIView.as_view(), name="applicationsCreate"),
    path("applications/", ApplicationsAPIView.as_view(), name="applications"),
    path("/cards", PatientsCardsAPIView.as_view(), name="cards")
]
