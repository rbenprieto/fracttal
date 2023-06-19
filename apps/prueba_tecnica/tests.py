from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from django.urls import reverse
import json
import pandas as pd
from apps.prueba_tecnica.utils import data_for_saving
from datetime import datetime


class MedicionesTestCase(APITestCase):
    """
    Test for util function data_for_saving, this is a certified that the function run correctly
    """

    # Defino parámetros iniciales y necesarios para la petición
    def setUp(self):
        self.data = [{'fecha': '2018-04-18', 'hora': '04:41:00', 'sensor': 'sensor_47', 'medicion': 29.513890000000004, 'estado': 'RECOVERING'}, {'fecha': '2018-04-18', 'hora': '04:42:00', 'sensor': 'sensor_47', 'medicion': 29.513890000000003, 'estado': 'RECOVERING'}]
        self.client = APIRequestFactory()

    # Hace el llamado a la función y compara los resultados recibidos con los esperados
    def test_mediciones_post_method(self):
        df = pd.DataFrame(self.data)
        response = data_for_saving(df)
        self.assertEqual(response[0]["sensor"], "sensor_47")
        self.assertEqual(response[0]["valor_medicion"], 29.513890000000004)
