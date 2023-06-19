from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError
import pandas as pd

from apps.prueba_tecnica.models import Medicion
from apps.prueba_tecnica.serializers import MedicionesSerializer
from apps.prueba_tecnica.utils import read_csv, processing_data, data_for_saving, read_csv_update


class MedicionesView(generics.ListCreateAPIView):
    """
    Endpoint to read and send new data about sensor measurements
    """

    serializer_class = MedicionesSerializer
    queryset = Medicion.objects.all()

    def get(self, request):
        # Llamo la función utilitaria para leer y obtener la data del csv
        data = read_csv()

        # Guardo la data estructurada en DB
        existing_data = Medicion.objects.filter(
            Q(sensor__in=[item["sensor"] for item in data])
            | Q(valor_medicion__in=[item["valor_medicion"] for item in data])
        )

        # Evito duplicar la información en cada llamado, sino solo cuando esa data no existe en DB
        if not existing_data.exists():
            serializer = self.serializer_class(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(
            {"detail": "Consulta exitosa", "data": data}, status=status.HTTP_200_OK
        )

    def post(self, request):
        # Obtengo la data enviada en json, la proceso y la imprimo en consola
        data = request.data
        df = processing_data(data)
        print(df)

        # Proceso la información para ahora guardarla en DB
        data_for_save = data_for_saving(df)
        serializer = self.serializer_class(data=data_for_save, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Guardado exitoso"}, status=status.HTTP_201_CREATED)


class MedicionesVariablesView(APIView):

    def post(self, request):
        file = request.FILES.get("sensor")

        # Verifico si se ha enviado un archivo CSV en la solicitud
        if not file:
            return Response({"error": "No se ha proporcionado ningún archivo"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.lower().endswith(".csv"):
                raise ValidationError({"error": "Este archivo debe ser de tipo csv (.csv)"})

        # Leer el archivo CSV usando Pandas
        try:
            df = pd.read_csv(file)
        except pd.errors.EmptyDataError:
            return Response({"error": "El archivo CSV está vacío"}, status=status.HTTP_400_BAD_REQUEST)
        except pd.errors.ParserError:
            return Response({"error": "Error al analizar el archivo CSV"}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar si el archivo CSV tiene las columnas necesarias
        required_columns = ['timestamp', 'sensor_07', 'sensor_47', 'machine_status']
        if not set(required_columns).issubset(df.columns):
            return Response({"error": "El archivo CSV no contiene todas las columnas requeridas"}, status=status.HTTP_400_BAD_REQUEST)

        data = read_csv_update(df)

        # Guardo la data estructurada en DB
        existing_data = Medicion.objects.filter(
            Q(sensor__in=[item["sensor"] for item in data])
            | Q(valor_medicion__in=[item["valor_medicion"] for item in data])
        )

        # Evito duplicar la información en cada llamado, sino solo cuando esa data no existe en DB
        if not existing_data.exists():
            serializer = self.serializer_class(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(
            {"detail": "Consulta exitosa", "data": data}, status=status.HTTP_200_OK
        )