from django.urls import path

from .views import MedicionesView, MedicionesVariablesView

urlpatterns = [
    path("measurements/", MedicionesView.as_view(), name="measurements"),
    path("measurements-update/", MedicionesVariablesView.as_view(), name="measurements-update"),
]
