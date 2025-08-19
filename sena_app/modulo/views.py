from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Actividad
from django.shortcuts import get_object_or_404

def lista_actividades(request):
    lista_actividades = Actividad.objects.all()
    total_actividades = Actividad.objects.count()
    return render(request, 'lista_actividades.html', {
        'lista_actividades': lista_actividades,
        'total_actividades': total_actividades,
    })

def detalles_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    return render(request, 'detalles_actividad.html', {
        'actividad': actividad,
    })

