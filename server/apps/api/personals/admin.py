from django.contrib import admin
from .models import (
  Applications,
  Cabinets,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule
)


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "typepr")

@admin.register(Cabinets)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("city", "num")

@admin.register(KRDSchedule)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("client", "date", "time_visit", "typePriem",)

@admin.register(RNDSchedule)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("client", "date", "time_visit", "typePriem",)

@admin.register(SCHSchedule)
class CabinetsAdmin(admin.ModelAdmin):
    list_display = ("client", "date", "time_visit", "typePriem",)