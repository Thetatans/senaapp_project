from .models import Actividad
from django.urls import path
from . import views

app_name = 'actividades'

urlpatterns = [
    path('lista_actividades/', views.lista_actividades, name='lista_actividades'),
    path('lista_actividades/actividad/<int:actividad_id>/', views.detalles_actividad, name='detalles_actividad'),
    path('crear_actividad/', views.ActividadFormView.as_view(), name='crear_actividad'),
    ]