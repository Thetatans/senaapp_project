from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código", help_text="Ingrese el código del programa de formación.")
    nombre = forms.CharField(max_length=200, label="Nombre", help_text="Ingrese el nombre del programa de formación.")
    nivel_formacion = forms.ChoiceField(choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formación del programa de formación.")
    modalidad = forms.ChoiceField(choices=Programa.MODALIDAD_CHOICES, label="Modalidad", help_text="Seleccione la modalidad del programa de formación.")
    duracion_meses = forms.IntegerField(min_value=0, label="Duración en Meses", help_text="Ingrese la duración del programa de formación en meses.")
    duracion_horas = forms.IntegerField(min_value=0, label="Duración en Horas", help_text="Ingrese la duración del programa de formación en horas.")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción", help_text="Ingrese la descripción del programa de formación.", required=False)
    competencias = forms.CharField(widget=forms.Textarea, label="Competencias a Desarrollar", help_text="Ingrese las competencias a desarrollar del programa de formación.")
    perfil_egreso = forms.CharField(widget=forms.Textarea, label="Perfil de Egreso", help_text="Ingrese el perfil de egreso del programa de formación.")
    requisitos_ingreso = forms.CharField(widget=forms.Textarea, label="Requisitos de Ingreso", help_text="Ingrese los requisitos de ingreso del programa de formación.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación", help_text="Ingrese el centro de formación del programa de formación.")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese el regional del programa de formación.")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, label="Estado", help_text="Seleccione el estado del programa de formación.")
    fecha_creacion = forms.DateField(label="Fecha de Creación", help_text="Ingrese la fecha de creación del programa de formación.")
    fecha_vista = forms.DateField(label="Fecha de Vista", help_text="Ingrese la fecha de vista del programa de formación.")
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        nivel_formacion = cleaned_data.get('nivel_formacion')
        modalidad = cleaned_data.get('modalidad')
        duracion_meses = cleaned_data.get('duracion_meses')
        duracion_horas = cleaned_data.get('duracion_horas')
        requisitos_ingreso = cleaned_data.get('requisitos_ingreso')
        centro_formacion = cleaned_data.get('centro_formacion')
        regional = cleaned_data.get('regional')
        estado = cleaned_data.get('estado')

        if not codigo or not nombre or not nivel_formacion or not modalidad or not duracion_meses or not duracion_horas or not requisitos_ingreso or not centro_formacion or not regional or not estado:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        return cleaned_data

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isdigit():
            raise forms.ValidationError("El código debe contener solo números.")
        return codigo
        
        
    def save(self):
        """Método para guardar el programa de formación en la base de datos"""
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                modalidad=self.cleaned_data['modalidad'],
                duracion_meses=self.cleaned_data['duracion_meses'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                descripcion=self.cleaned_data['descripcion'],
                competencias=self.cleaned_data['competencias'],
                perfil_egreso=self.cleaned_data['perfil_egreso'],
                requisitos_ingreso=self.cleaned_data['requisitos_ingreso'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
                fecha_creacion=self.cleaned_data['fecha_creacion'],
                fecha_registro=self.cleaned_data.get('fecha_vista', "")
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el programa de formación: {str(e)}")