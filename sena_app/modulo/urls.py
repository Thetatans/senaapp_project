from .models import Actividad
from django.urls import path
from . import views

app_name = 'actividades'

urlpatterns = [
    path('actividad/', views.lista_actividades, name='lista_actividades'),
    path('actividades/actividad/', views.detalles_actividad, name='detalle_actividad'),
    ]