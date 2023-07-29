from django import forms
from ujc.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget


class ProvForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ["nombreProvincia", "primersecretario"]


class EscolaridadForm(forms.ModelForm):
    class Meta:
        model = Escolaridad
        fields = ["tipoescolaridad"]


class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ["direccion", "cantDelegados"]


class DelegadoForm(forms.ModelForm):
    class Meta:
        model = Delegado
        fields = ["nombreDelegado", "edad", "sexo", "telefono", "direccion",
                  "fechaIngresoUjc", "responsabilidad", "centroTrabajo", "limitacion", "provincia",
                  "escolaridad", "casa"]

        # widgets = {
        #     #'fechaIngresoUjc': forms.DateTimeInput()
        #     'fechaIngresoUjc': forms.DateInput(attrs = {'class': 'datepicker',
        #         'type':'date'}, format='%d/%m/%Y')
        # }


class IntegrantesNucleoForm(forms.ModelForm):
    #
    # nombre = forms.CharField(max_length=35)
    # casa = forms.CharField(max_length=50)
    # sexo = forms.CharField(max_length=10)
    # fechaNac = forms.DateField(widget=AdminDateWidget)
    class Meta:
        model = IntegrantesNucleo
        fields = ["nombre", "fechaNac", "casa","sexo"]


class JefeNucleoForm(forms.ModelForm):
    
    class Meta:
        #CHOICES= (('Femenino', 'femenino'),('MASCULINO', 'masculino'))
        model = JefeNucleo
        fields = ["ocupacion", "edad", "integrante"]

        # widget={
        # 'sexo':forms.Select(choices=CHOICES)
        # }

class EmbarazadasForm(forms.ModelForm):
    class Meta:
        model = Embarazadas
        fields = ["nombreDelegado", "edad", "sexo", "telefono", "direccion",
                  "fechaIngresoUjc", "responsabilidad", "centroTrabajo", "limitacion", "provincia",
                  "escolaridad", "casa", "posibleFechaDeParto"]


class RegistroForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        widgets = {
            'password': forms.PasswordInput()
        }

        #		fields = ["nombreProvincia"]


        # class ProvinciaForm(forms.Form):
        # 	nombreProvinciaF = forms.CharField(max_length=30)
        # 	primersecretarioF = forms.CharField(max_length=30)
