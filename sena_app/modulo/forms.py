from django import forms
from .models import Actividad

class ActividadForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre de la Actividad", help_text="Ingrese el nombre de la actividad extracurricular.")
    categoria = forms.ChoiceField(choices=Actividad.CATEGORIA_CHOICES, label="Categoría", help_text="Seleccione la categoría de la actividad extracurricular.")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción de la Actividad", help_text="Ingrese la descripción de la actividad extracurricular.")
    fecha_inicio = forms.DateField(label="Fecha de Inicio", help_text="Ingrese la fecha de inicio de la actividad extracurricular.")
    fecha_fin = forms.DateField(label="Fecha de Finalización", help_text="Ingrese la fecha de finalización de la actividad extracurricular.")
    centro_formacion = forms.CharField(max_length=200, label="Centro de Formación", help_text="Ingrese el centro de formación de la actividad extracurricular.")
    regional = forms.CharField(max_length=100, label="Regional", help_text="Ingrese el regional de la actividad extracurricular.")    
    estado = forms.ChoiceField(choices=Actividad.ESTADO_CHOICES, label="Estado", help_text="Seleccione el estado de la actividad extracurricular.")
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        categoria = cleaned_data.get('categoria')
        descripcion = cleaned_data.get('descripcion')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        centro_formacion = cleaned_data.get('centro_formacion')
        regional = cleaned_data.get('regional')
        estado = cleaned_data.get('estado')

        if not nombre or not categoria or not descripcion or not fecha_inicio or not fecha_fin or not centro_formacion or not regional or not estado:
            raise forms.ValidationError("Todos los campos son obligatorios.")

        return cleaned_data

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre:
            raise forms.ValidationError("El nombre de la actividad no puede estar vacío.")
        return nombre
        
    def clean_categoria(self):
        categoria = self.cleaned_data['categoria']
        if not categoria:
            raise forms.ValidationError("La categoría de la actividad no puede estar vacía.")
        return categoria
        
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if not descripcion:
            raise forms.ValidationError("La descripción de la actividad no puede estar vacía.")
        return descripcion
        
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']
        if not fecha_inicio:
            raise forms.ValidationError("La fecha de inicio de la actividad no puede estar vacía.")
        return fecha_inicio
        
    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data['fecha_fin']
        if not fecha_fin:
            raise forms.ValidationError("La fecha de finalización de la actividad no puede estar vacía.")
        return fecha_fin
        
    def clean_centro_formacion(self):
        centro_formacion = self.cleaned_data['centro_formacion']
        if not centro_formacion:
            raise forms.ValidationError("El centro de formación de la actividad no puede estar vacío.")
        return centro_formacion
        
    def clean_regional(self):
        regional = self.cleaned_data['regional']
        if not regional:
            raise forms.ValidationError("El regional de la actividad no puede estar vacío.")
        return regional
        
    def clean_estado(self):
        estado = self.cleaned_data['estado']
        if not estado:
            raise forms.ValidationError("El estado de la actividad no puede estar vacío.")
        return estado

    def save(self):
        """Método para guardar la actividad en la base de datos"""
        try:
            actividad = Actividad.objects.create(
                nombre=self.cleaned_data['nombre'],
                categoria=self.cleaned_data['categoria'],
                descripcion=self.cleaned_data['descripcion'],
                fecha_inicio=self.cleaned_data['fecha_inicio'],
                fecha_fin=self.cleaned_data['fecha_fin'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                regional=self.cleaned_data['regional'],
                estado=self.cleaned_data['estado'],
            )
            return actividad
        except Exception as e: 
            raise forms.ValidationError(f"Error al crear la actividad: {str(e)}")  