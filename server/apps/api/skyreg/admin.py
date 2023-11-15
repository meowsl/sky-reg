from django.contrib import admin

from .models import (
  KRDSchedule,
  RNDSchedule,
  SCHSchedule,
  Cabinets)


@admin.register(RNDSchedule)
class RNDScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)


@admin.register(KRDSchedule)
class KRDScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)


@admin.register(SCHSchedule)
class SCHScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)

@admin.register(Cabinets)
class CabinetsAdmin(admin.ModelAdmin):
  list_display = ('city', 'num')


