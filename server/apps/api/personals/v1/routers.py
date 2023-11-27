from django.urls import path
from .views import ApplicationsCreateAPIView, ApplicationsAPIView, ApplicationsUpdateAPIViev

app_name = "personals"

urlpatterns = [
    path("applications/create/", ApplicationsCreateAPIView.as_view()),
    path("applications/list/", ApplicationsAPIView.as_view(), name="applications"),
    path("applications/update/<int:pk>", ApplicationsUpdateAPIViev.as_view(), name="update")
]
