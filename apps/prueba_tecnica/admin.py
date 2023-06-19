from django.contrib import admin

from .models import Medicion


@admin.register(Medicion)
class MedicionAdmin(admin.ModelAdmin):
    model = Medicion
    list_display = ("fecha", "sensor", "machine_status", "valor_medicion")
    list_display_links = list_display
