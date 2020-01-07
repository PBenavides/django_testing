from __future__ import unicode_literals

from djongo import models

class Nodos(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=False, auto_now=True)

    id_nodo = models.IntegerField(default=10, null=True)
    nro_sensores = models.IntegerField(default=3,null=True)
    id_piscina = models.IntegerField(default=0, null=True)

    def __str__(self):
        template = '{0.id_nodo}'
        return template.format(self)