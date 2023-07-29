from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from ujc.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Examples:
    # url(r'^$', 'CongresoUJC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ujc.views.home', name='home'),
    url(r'^provinciaInsertar/', 'ujc.views.provinciaInsertar', name='provinciaInsertar'),
    url(r'^sobrenosotros/', 'ujc.views.sobre', name='sobre'),
    url(r'^listadoProvincia/', 'ujc.views.listadoProvincia', name='listadoProvincia'),
    url(r'^listadoDelegado/$', listadoDelegado),
    url(r'^delegadoInsertar/$', delegadoInsertar),
    url(r'^listadoEscolaridad/$', listadoEscolaridad),
    url(r'^listadoCasa/$', listadoCasa),
    url(r'^casaInsertar/$', casaInsertar),
    url(r'^listadoEmbarazadas/$', listadoEmbarazadas),
    url(r'^embarazadasInsertar/$', embarazadasInsertar),
    url(r'^listadoIntegrantes/$', listadoIntegrantes),
    url(r'^listadoJefeN/$', listadoJefeN),
    url(r'^jefenucleoInsertar/$', jefenucleoInsertar),
    url(r'^integrantesInsertar/$', integrantesInsertar),
    url(r'^listadoDelegadosLimitados/$', listadoDelegadosLimitados),
    url(r'^listadoDelegados14_20/$', listadoDelegados14_20),
    url(r'^listadoDelegados21_25/$', listadoDelegados21_25),
    url(r'^listadoESC_sec/$', listadoESC_sec),
    url(r'^ubicacionDeleg/$',ubicacionDeleg),

    url(r'^delegados_provincia/$', 'ujc.views.delegados_provincia', name='delegados_provincia'),

    url(r'^delegados_provincia$/', delegados_provincia, name='delegados_provincia'),
    url(r'^registrarse/$', 'ujc.views.registro_usuario', name='registrarse'),
    #url(r'^accounts/logout$', logout, name='logout'),
    url(r'^accounts/logout$' , logout, { 'next_page' : 'ujc.views.home' }, name = 'logout'),
    url(r'^accounts/login$', login, {'template_name': 'usuario/login.html'}, name='login'),

    ##############################################################

    # url(r'^registro_usuario/$', registro_usuario),

    url(r'^eliminar/$', eliminar),
    url(r'^editar_Delegado/(\d+)$', 'ujc.views.editar_Delegado', name='editar_Delegado'),
    url(r'^eliminar_Delegado/(\d+)$', 'ujc.views.eliminar_Delegado', name='eliminar_Delegado'),
    url(r'^editar_Embarazada/(\d+)$', 'ujc.views.editar_Embarazada', name='editar_Embarazada'),
    url(r'^eliminar_Embarazada/(\d+)$', 'ujc.views.eliminar_Embarazada', name='eliminar_Embarazada'),
    url(r'^editar_Integrante/(\d+)$', 'ujc.views.editar_Integrante', name='editar_Integrante'),
    url(r'^eliminar_Integrante/(\d+)$', 'ujc.views.eliminar_Integrante', name='eliminar_Integrante'),
    url(r'^editar_Jefe/(\d+)$', 'ujc.views.editar_Jefe', name='editar_Jefe'),
    url(r'^eliminar_Jefe/(\d+)$', 'ujc.views.eliminar_Jefe', name='eliminar_Jefe'),
    url(r'^editar_Casa/(\d+)$', 'ujc.views.editar_Casa', name='editar_Casa'),
    url(r'^eliminar_Casa/(\d+)$', 'ujc.views.eliminar_Casa', name='eliminar_Casa'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
