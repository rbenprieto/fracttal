from django.db import models


class Medicion(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    fecha = models.DateTimeField()
    sensor = models.CharField(max_length=50)
    valor_medicion = models.DecimalField(max_digits=30, decimal_places=20)
    machine_status = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Medición"
        verbose_name_plural = "Mediciones"
