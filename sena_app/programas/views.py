from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.shortcuts import get_object_or_404

from programas.forms import ProgramaForm
from django.views import generic
from django.contrib import messages
from django.views.generic import FormView

# Create your views here.

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
    'lista_programas': lista_programas,
    'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    
    return HttpResponse(template.render(context, request))


class ProgramaFormView(generic.FormView):
    template_name = 'crear_programa.html'
    form_class = ProgramaForm
    success_url = "../programasprogramas/"
    
    def form_valid(self, form):
        #guardar el programa
        programa = form.save()
        
        #agregar mensaje de éxito
        messages.success(
            self.request, 
            f'El programa {programa.nombre} ha sido registrado exitosamente.'
        )
        
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)
    
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import InstructorForm
# from .models import Instructor

# def crear_instructor(request):
#     """Vista para crear un nuevo instructor"""
#     if request.method == 'POST':
#         form = InstructorForm(request.POST)
#         if form.is_valid():
#             try:
#                 instructor = form.save()
#                 messages.success(
#                     request, 
#                     f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
#                 )
#                 return redirect('lista_instructores')  # Cambia por tu URL de lista
#             except Exception as e:
#                 messages.error(request, f'Error al guardar el instructor: {str(e)}')
#         else:
#             messages.error(request, 'Por favor, corrija los errores en el formulario.')
#             # Para depuración, imprime los errores
#             print("Errores del formulario:", form.errors)
#     else:
#         form = InstructorForm()
    
#     return render(request, 'crear_instructor.html', {
#         'form': form,
#         'titulo': 'Registrar Nuevo Instructor'
#     })
    