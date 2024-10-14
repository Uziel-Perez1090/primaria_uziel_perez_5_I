from django.db import models

# Create your models here.

class Alumno(models.model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre (s)")
    fecha_ingreso=models.DateField(verbose_name="fecha de nacimiento",null=False,blank=False)
