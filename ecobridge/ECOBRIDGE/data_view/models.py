from django.db import models

# Create your models here.

#Este es mi modelo de data 
class Sensores(models.Model):
    nombre = models.CharField(max_length=120)
    id_mcu = models.CharField(max_length=12)
    nro_piscina = models.DecimalField(decimal_places=0,max_digits=4)
    nro_sensores = models.DecimalField(max_length=3,decimal_places=2,max_digits=5)
    activo = models.BooleanField(default=False)
    temperatura = models.DecimalField(decimal_places=2,max_digits=4)
    ph = models.DecimalField(decimal_places=2,max_digits=4)