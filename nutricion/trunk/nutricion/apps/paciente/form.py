from django import forms
from apps.paciente.models import Paciente

class RegistroPacienteUno(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            #Datos generales del paciente
        'nombres',
        'apellidos',
        'expediente', 
        'edad' ,
        'fechaNAc', 
        'estadocivil',
        'ocupacion' ,
        'telefono',
        'correo' ,
        ]
        labels = {
            'nombres' : 'Nombre',
            'apellidos' : 'Apellidos',
            'expediente' : 'Numero de Expediente ',
            'edad' : 'Edad',
            'fechaNAc' : 'Fecha de Nacimiento',
            'estadocivil': 'Estado Civil',
            'ocupacion' : 'Ocupacion',
            'telefono': 'Telefono',
            'correo' : 'Correo',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'expediente' : forms.TextInput(attrs={'class': 'form-control'}),
            'edad' : forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNAc' : forms.TextInput(attrs={'class': 'form-control'}),
            'estadocivil': forms.RadioChoiceInput(attrs={'class': 'form-control'}),
            'ocupacion' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo' : forms.TextInput(attrs={'class': 'form-control'}),
            'cita': forms.Select(attrs={'class': 'form-control'}),
        }

