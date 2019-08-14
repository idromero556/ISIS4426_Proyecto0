from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    nombre=models.CharField(max_length=200)
    lugar=models.CharField(max_length=300)
    direccion=models.CharField(max_length=300)
    fecha_ini=models.DateField()
    fecha_fin=models.DateField()
    categoria=models.CharField(max_length=60)
    tipo=models.CharField(max_length=60)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return 'Evento: '+self.nombre

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'categoria', 'lugar', 'direccion', 'fecha_ini', 'fecha_fin', 'tipo']

