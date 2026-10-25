from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'prueba.html')

