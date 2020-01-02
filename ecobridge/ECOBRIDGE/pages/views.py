from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
# Create your views here.

def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

def display_data_view(request, *args, **kwargs):
    return render(request, "display-data.html",{})

# La funcion get_data_http detectara si el reques es un POST. Si lo es, 
# hara un decode del request(pq viene en bytes) para luego parsear todas las palabras que esten entre
# comillas. Asignara cada palabra segun su id o llave detectando quien va primero (y asumiendo que las llaves
# siempre van primero). Luego, asignara estas llaves a un contexto para que sea imprimido en el html.


#El comando curl para hacer el post es:
#curl -i -X POST 'Content-Type: application/json' -d '{"name":"Pabloski", "action":"testeando","message":"gaaa"}' http://127.0.0.1:8000/get/

def get_data_http(request,*args,**kwargs):
    context = {"name":"Aun no hay data","action":"Aun no hay data","message":"aun no hay data"}
    if request.method == 'POST':
        lista_llaves = []
        lista_valores = []
        string = request.body.decode('utf-8')
        regex = '"([^"]*)"'
        lista_llaves_y_valores = re.findall(regex,string)
        for id_llave, valor in enumerate(lista_llaves_y_valores):
            if int(id_llave) % 2:
                lista_valores.append(valor)
            else:
                lista_llaves.append(valor)
        context = dict(zip(lista_llaves,lista_valores))
        print('los valores son:', lista_valores)
        print('las llaves son:', lista_llaves)
        
    return render(request,"get-data.html",context)


