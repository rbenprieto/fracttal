from django.urls import path
from .views import MedicionesView

urlpatterns = [
    path("upload/", MedicionesView.as_view(), name="file-upload"),
]
