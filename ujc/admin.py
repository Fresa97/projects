from django.contrib import admin

from .forms import ProvForm

from models import Provincia
from models import Escolaridad
from models import Casa
from models import Delegado
from models import IntegrantesNucleo
from models import JefeNucleo
from models import Embarazadas
from models import Sexo
from models import Limitacion


#Register your models here.
class AdminProvincia(admin.ModelAdmin ):
    list_display = ["__str__","nombreProvincia", "primersecretario"]
    form = ProvForm

    # class Meta():
    #     model = Provincia

class AdminEscolaridad(admin.ModelAdmin ):
    list_display = ["__str__","tipoescolaridad"]
    class Meta():
        model = Escolaridad


class AdminCasa(admin.ModelAdmin ):
   list_display = ["__str__","direccion"]
   class Meta():
       model = Casa

class AdminDelegado(admin.ModelAdmin ):
    list_display = ["__str__","nombreDelegado"]
    class Meta():
        model = Delegado

class AdminIntegrantesNucleo(admin.ModelAdmin ):
    list_display = ["__str__","nombre"]
    class Meta():
        model = IntegrantesNucleo

class AdminJefeNucleo(admin.ModelAdmin ):
    list_display = ["__str__","integrante"]
    class Meta():
        model = JefeNucleo

class AdminEmbarazadas(admin.ModelAdmin ):
    list_display = ["__str__","posibleFechaDeParto"]
    class Meta():
        model = Embarazadas

class AdminLimitacion(admin.ModelAdmin ):
    list_display = ["__str__","tipo"]
    class Meta():
        model = Limitacion

class AdminSexo(admin.ModelAdmin ):
    list_display = ["__str__","tipo"]
    class Meta():
        model = Sexo



admin.site.register(Provincia, AdminProvincia)
admin.site.register(Escolaridad, AdminEscolaridad)
admin.site.register(Casa, AdminCasa)
admin.site.register(Delegado, AdminDelegado)
admin.site.register(IntegrantesNucleo, AdminIntegrantesNucleo)
admin.site.register(JefeNucleo, AdminJefeNucleo)

admin.site.register(Sexo, AdminSexo)
admin.site.register(Limitacion, AdminLimitacion)

admin.site.register(Embarazadas, AdminEmbarazadas)