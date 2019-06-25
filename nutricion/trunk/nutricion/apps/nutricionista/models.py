from django.db import models
from apps.login.models import Usuario

#from apps.login.models import Usurio
# Create your models here.

class Nutricionista(models.Model):

    #usa la llave primaria por defecto del framework
    nombre = models.CharField(max_length = 40)
    apellidos = models.CharField(max_length = 40)
    correo = models.CharField(max_length = 40)
    telefono = models.CharField(max_length = 8)

    #Haciendo relacion de composicion 1..*
    login = models.ForeignKey(Usuario, on_delete = models.CASCADE,  blank = True)
