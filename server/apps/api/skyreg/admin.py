from django.contrib import admin

from .models import RNDCabinets, KRDCabinets, SCHCabinets

@admin.register(RNDCabinets)
class RNDCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num", )

@admin.register(KRDCabinets)
class KRDCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num", )

@admin.register(SCHCabinets)
class SCHCabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_num",)



