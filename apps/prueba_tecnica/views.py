from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from apps.prueba_tecnica.models import Medicion
from apps.prueba_tecnica.serializers import MedicionesSerializer
from apps.prueba_tecnica.utils import read_csv


class MedicionesView(generics.ListCreateAPIView):
    """
    Endpoint to read and send new data about sensor measurements
    """

    serializer_class = MedicionesSerializer
    queryset = Medicion.objects.all()

    def get(self, request):
        df = read_csv()
        print("df: ", df)
        return Response("holis GET")

    def post(self, request):
        return Response("holis")
