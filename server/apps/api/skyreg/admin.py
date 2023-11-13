from django.contrib import admin

from .models import (
  RNDCabinets,
  KRDCabinets,
  SCHCabinets,
  KRDSchedule,
  RNDSchedule,
  SCHSchedule)

# Ростов-на-Дону
@admin.register(RNDCabinets)
class RNDCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num", )

@admin.register(RNDSchedule)
class RNDScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)

# Краснодар
@admin.register(KRDCabinets)
class KRDCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num", )

@admin.register(KRDSchedule)
class KRDScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)

# Сочи
@admin.register(SCHCabinets)
class SCHCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num",)

@admin.register(SCHSchedule)
class SCHScheduleAdmin(admin.ModelAdmin):
  list_display = ("date",)




