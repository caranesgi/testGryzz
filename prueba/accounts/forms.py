from dataclasses import fields
import imp
from pyexpat import model
from django.forms import ModelForm
from .models import *

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'
