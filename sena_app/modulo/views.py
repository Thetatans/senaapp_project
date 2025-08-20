from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView
from .forms import ActividadForm
from .models import Actividad

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Actividad
from django.shortcuts import get_object_or_404

def lista_actividades(request):
    lista_actividades = Actividad.objects.all()
    total_actividades = Actividad.objects.count()
    template = loader.get_template('lista_actividades.html')
    context = {
        'lista_actividades': lista_actividades,
        'total_actividades': total_actividades,
    }
    return HttpResponse(template.render(context, request))

def detalles_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    template = loader.get_template('detalles_actividad.html')
    
    context = {
        'actividad': actividad,
    }
    
    return HttpResponse(template.render(context, request))

class ActividadFormView(FormView):
    template_name = 'crear_actividad.html'
    form_class = ActividadForm
    success_url = "../modulolista_actividades/"
    
    def form_valid(self, form):
        # Guardar la actividad
        actividad = form.save()
        
        # Agregar mensaje de éxito
        messages.success(
            self.request, 
            f'La actividad {actividad.nombre} ha sido registrada exitosamente.'
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
    
# Vista para eliminar actividad - CORREGIDA
class ActividadDeleteView(generic.DeleteView):
    model = Actividad
    template_name = 'confirmar_eliminacion_actividad.html'  # Template de confirmación
    success_url = "/modulolista_actividades/"
    context_object_name = 'actividad'
    
    def delete(self, request, *args, **kwargs):
        # Obtener el objeto antes de eliminarlo para mostrar el mensaje
        self.object = self.get_object()
        nombre_actividad = self.object.nombre
        
        # Llamar al método delete del padre
        response = super().delete(request, *args, **kwargs)
        
        # Agregar mensaje de éxito
        messages.success(
            self.request,
            f'La actividad "{nombre_actividad}" ha sido eliminada exitosamente.'
        )
        
        return response