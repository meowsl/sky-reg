from django.contrib import admin

from .models import Applications, Cabinets

@admin.register(Cabinets)
class CabinetsAdmin(admin.ModelAdmin):
  list_display = ("cabinet_floor", "cabinet_num")

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "type_priem")

