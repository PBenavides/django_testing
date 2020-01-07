from django.shortcuts import render
from django.http import HttpResponse

from .models import Nodos
# Create your views here.

# Asigno Nodos.objects.get(id=1) para solo mostrar las vistas del id 1
def view_nodos(request,*args,**kwargs):
    nodo = Nodos.objects.get(id=1)
    context = {
        'id_nodo': nodo.id_nodo ,
        'nro_sensores': nodo.nro_sensores,
        'id_piscina':nodo.id_piscina
    }
    return render(request, "nodos.html",context)