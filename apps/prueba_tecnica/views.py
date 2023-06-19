from django.shortcuts import render
from rest_framework import generics
from .serializers import MedicionesSerializer
from .models import Medicion
from rest_framework.response import Response

class MedicionesView(generics.ListCreateAPIView):
    serializer_class = MedicionesSerializer
    queryset = Medicion.objects.all()

    def get(self, request):
        return Response("holis GET")
    
    def post(self, request):
        return Response("holis")

