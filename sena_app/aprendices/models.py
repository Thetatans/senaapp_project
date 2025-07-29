from django.db import models

class aprendiz(models.Model):
# Create your models here.
    documento_identidad = models.CharField(max_length=25, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    programa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"