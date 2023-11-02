from django.contrib import admin
from .models import PatientsCards, Applications

@admin.register(PatientsCards)
class PatientsCards(admin.ModelAdmin):
    list_display = (
        "lastname",
        "firstname",
        "midname",
        "sex",
        "birthday",
        "phone",
        "address_obl",
        "address_city",
        "address_street",
        "address_house",
        "address_korpus",
        "address_flat",
        "work_place",
        "work_position",
        "is_dependent"
    )

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "type_priem")