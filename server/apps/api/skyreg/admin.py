from django.contrib import admin

from .models import Applications

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "type_priem")
