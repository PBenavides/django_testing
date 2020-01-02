from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

def display_data_view(request, *args, **kwargs):
    return render(request, "display-data.html",{})

def get_data_http(request,*args,**kwargs):
    return render(request,"get-data.html",{})