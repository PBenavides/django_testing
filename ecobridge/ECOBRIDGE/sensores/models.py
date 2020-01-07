from djongo import models

class Sensores_data(models.Model):
    date_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=50)
    actions = models.CharField(max_length=20)
    message = models.CharField(max_length=120)
    numero = models.DecimalField(decimal_places=4,max_digits=5)