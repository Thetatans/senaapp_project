from django.db import models


class Actividad(models.Model):
    CATEGORIA_CHOICES = [
        ('DEP', 'Deportes'),
        ('CUL', 'Cultural'),
        ('TEC', 'Tecnológica'),
        ('ART', 'Artística'),
        ('AMB', 'Ambiental'),
        ('SOC', 'Social'),
        ('LID', 'Liderazgo'),
        ('EMP', 'Emprendimiento'),
        ('VOL', 'Voluntariado'),
        ('CIE', 'Científica'),
    ]

    ESTADO_CHOICES = [
        ('PLA', 'Planificada'),
        ('ACT', 'Activa'),
        ('SUS', 'Suspendida'),
        ('FIN', 'Finalizada'),
        ('CAN', 'Cancelada'),
    ]

    # Información básica
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la Actividad")
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, verbose_name="Categoría")
    descripcion = models.TextField(verbose_name="Descripción de la Actividad")
    
    # Fechas
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalización")
    
    # Ubicación institucional
    centro_formacion = models.CharField(max_length=200, verbose_name="Centro de Formación")
    regional = models.CharField(max_length=100, verbose_name="Regional")
    
    # Estado
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PLA', verbose_name="Estado")

    class Meta:
        verbose_name = "Actividad Extracurricular"
        verbose_name_plural = "Actividades Extracurricular"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_categoria_display()}"

    def is_activa(self):
        """Verifica si la actividad está activa"""
        return self.estado == 'ACT'

1