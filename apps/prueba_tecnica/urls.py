from django.urls import path

from .views import MedicionesView

urlpatterns = [
    path("measurements/", MedicionesView.as_view(), name="measurements"),
]
