from django.contrib.auth.views import password_change
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ujc.models import *
from ujc.forms import *
import sqlite3
from django.shortcuts import redirect


def home(request):
    titulo = "Home"

    context = {
        "titulo_template": titulo,
    }

    return render(request, "base.html", context)


# def delegadoInsertar(request):
#     if request.method == "POST":
#         formulario = DelegadoForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('/listadoDelegado')
#     else:
#         formulario = DelegadoForm()
#     return render(request, 'new.html', {'formulario': formulario, 'title': 'Nueva Cuenta de Entidades'})


def delegadoInsertar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        form = DelegadoForm(request.POST or None)
        titulo = "Nuevo Delegado"
        context = {
            "form": form,
            "titulo": titulo
        }

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            return redirect('/listadoDelegado')

        return render(request, "delegados/new.html", context)


def provinciaInsertar(request):
    form = ProvForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        return redirect('/listadoProvincia')

    return render(request, "provincia/new.html", context)


def casaInsertar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        form = CasaForm(request.POST or None)
        titulo = "Nueva Casa"
        context = {
            "form": form,
            "titulo": titulo
        }

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()

            return redirect('/listadoCasa')

        return render(request, "casa/new.html", context)


def embarazadasInsertar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        form = EmbarazadasForm(request.POST or None)
        titulo = "Nueva Embarazadas"
        context = {
            "form": form,
            "titulo": titulo
        }

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            return redirect('/listadoEmbarazadas')

        return render(request, "embarazadas/new.html", context)


def jefenucleoInsertar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        form = JefeNucleoForm(request.POST or None)
        titulo = "Nuevo Jefe"
        context = {
            "form": form,
            "titulo": titulo
        }

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            return redirect('/listadoJefeN')

        return render(request, "jefenucleo/new.html", context)


def integrantesInsertar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        form = IntegrantesNucleoForm(request.POST or None)
        titulo = "Nuevo Integrante"
        context = {
            "form": form,
            "titulo": titulo
        }

        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            return redirect('/listadoIntegrantes')

        return render(request, "integrantes_nucleo/new.html", context)


def listadoDelegado(request):
    listado = Delegado.objects.all()
    return render(request, 'delegados/index.html',
                  {'listado': listado, 'title': 'Delegado', 'url': '/listadoDelegado'})


def listadoProvincia(request):
    listado = Provincia.objects.all()
    return render(request, 'provincia/index.html', {'listado': listado,
                                                    'title': 'Provincia', 'url': '/listadoProvincia'})


def listadoEscolaridad(request):
    listado = Escolaridad.objects.all()
    return render(request, 'escolaridad/index.html', {'listado': listado,
                                                      'title': 'Escolaridad', 'url': '/listadoEscolaridad'})


def listadoCasa(request):
    listado = Casa.objects.all()
    return render(request, 'casa/index.html', {'listado': listado,
                                               'title': 'Casa', 'url': '/listadoCasa'})


def listadoEmbarazadas(request):
    listado = Embarazadas.objects.all()
    return render(request, 'embarazadas/index.html', {'listado': listado,
                                                      'title': 'Embarazadas', 'url': '/listadoEmbarazadas'})


def listadoIntegrantes(request):
    listado = IntegrantesNucleo.objects.all()
    return render(request, 'integrantes_nucleo/index.html', {'listado': listado,
                                                             'title': 'IntegrantesNucleo',
                                                             'url': '/listadoIntegrantes'})


def listadoJefeN(request):
    listado = JefeNucleo.objects.all()
    return render(request, 'jefenucleo/index.html', {'listado': listado,
                                                     'title': 'JefeNucleo', 'url': '/listadoJefeN'})


def listadoDelegadosLimitados(request):
    d = Delegado.objects.all()
    # e = Embarazadas.objects.all()
    listado = []

    titulo = "Delegados Limitados"

    context = {
        "titulo_template": titulo,
    }

    for rec in d:
        if rec.getLimitacion() == "Si":
            listado.append(rec)
    # for rec in e:
    #     if rec.getLimitacion() == "si":
    #         listado.append(rec)

    return render(request, 'delegados/limitados.html', {'listado': listado,
                                                        'titulo': titulo, 'title': 'Delegado',
                                                        'url': '/listadoDelegadosLimitados'})


def listadoDelegados14_20(request):
    d = Delegado.objects.all()
    # e = Embarazadas.objects.all()
    listado = []

    titulo = "Delegados con edad entre 14 y 20"

    context = {
        "titulo_template": titulo,
    }

    for rec in d:
        if rec.getEdad() >= 14 and rec.getEdad() <= 20:
            listado.append(rec)
    # for rec in e:
    #     if rec.getEdad() >= 14 and rec.getEdad() <= 20:
    #         listado.append(rec)

    return render(request, 'delegados/delegadosEdad.html', {'listado': listado,
                                                            'titulo': titulo, 'title': 'Delegado',
                                                            'url': '/listadoDelegados14_20'})


def listadoDelegados21_25(request):
    d = Delegado.objects.all()

    listado = []
    titulo = "Delegados con edad entre 21 y 25"

    context = {
        "titulo_template": titulo,
    }
    for rec in d:
        if rec.getEdad() >= 21 and rec.getEdad() <= 25:
            listado.append(rec)

    return render(request, 'delegados/delegadosEdad.html', {'listado': listado,
                                                            'titulo': titulo, 'title': 'Delegado',
                                                            'url': '/listadoDelegados21_25'})


def listadoESC_sec(request):
    d = Delegado.objects.all()
    e = Escolaridad.objects.all()
    listado = []
    selected_item = ""
    if request.method == 'POST':
        selected_item = request.POST["esc"]
        for deleg in d:
            if deleg.escolaridad.tipoescolaridad == selected_item:
                listado.append(deleg)
        return render(request, 'delegados/delegados_escolaridad.html',
                      {'listado': listado, 'e': e, 'selected_item': selected_item,
                       'url': '/delegados_provincia'})
    else:
        return render(request, 'delegados/delegados_escolaridad.html', {'e': e, 'selected_item': selected_item,
                                                                       'url': '/listadoESC_sec'})

def ubicacionDeleg(request):
    d = Delegado.objects.all()
    listado = []
    selected_item = ""
    if request.method == 'POST':
        selected_item = request.POST["deleg"]
        for deleg in d:
            if deleg.nombreDelegado == selected_item:
                listado.append(deleg)
        return render(request, 'delegados/delegados_ubicacion.html',
                      {'listado': listado, 'd': d, 'selected_item': selected_item,
                       'url': '/delegados_provincia'})
    else:
        return render(request, 'delegados/delegados_ubicacion.html', {'d': d, 'selected_item': selected_item,
                                                                       'url': '/ubicacionDeleg'})



def delegados_provincia(request):
    p = Provincia.objects.all()

    if request.method == 'POST':
        selected_item = request.POST["prov"]
        listado = Delegado.objects.filter(provincia=selected_item)
        return render(request, 'delegados/deleagados_provincia.html',
                      {'listado': listado, 'p': p, 'selected_item': selected_item,
                       'url': '/delegados_provincia'})
    else:
        return render(request, 'delegados/deleagados_provincia.html', {'p': p,
                                                                       'url': '/delegados_provincia'})


def eliminar(request):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        d = Delegado.objects.get(id)
        d.delete()
        listado = []

        return render(request, 'delegados/limitados.html', {'listado': listado,
                                                            'title': 'Delegado', 'url': '/eliminar'})


def sobre(request):
    titulo = "Sobre Nosotros"

    context = {
        "titulo_template": titulo,
    }

    return render(request, "sobre.html", context)


def editar_Delegado(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        temp = Delegado.objects.get(id=id_d)
        titulo = "Editar Delegado"
        if request.method == "POST":
            form = DelegadoForm(request.POST, instance=temp)
            if form.is_valid():
                form.save()
            return redirect('/listadoDelegado')
        else:
            form = DelegadoForm(instance=temp)
        return render(request, 'delegados/new.html', {'form': form, "titulo": titulo})


def eliminar_Delegado(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        delegado = Delegado.objects.get(id=id_d)
        delegado.delete()
        return redirect('/listadoDelegado')


def editar_Casa(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        temp = Casa.objects.get(id=id_d)
        titulo = "Editar Casa"
        if request.method == "POST":
            form = CasaForm(request.POST, instance=temp)
            if form.is_valid():
                form.save()
            return redirect('/listadoCasa')
        else:
            form = CasaForm(instance=temp)
        return render(request, 'casa/new.html', {'form': form, "titulo": titulo})


def eliminar_Casa(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        delegado = Casa.objects.get(id=id_d)
        delegado.delete()
        return redirect('/listadoCasa')


def eliminar_Embarazada(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        delegado = Embarazadas.objects.get(id=id_d)
        delegado.delete()
        return redirect('/listadoEmbarazadas')


def editar_Embarazada(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        temp = Embarazadas.objects.get(id=id_d)
        titulo = "Editar Embarazadas"
        if request.method == "POST":
            form = EmbarazadasForm(request.POST, instance=temp)
            if form.is_valid():
                form.save()
            return redirect('/listadoEmbarazadas')
        else:
            form = EmbarazadasForm(instance=temp)
        return render(request, 'embarazadas/new.html', {'form': form, "titulo": titulo})


def eliminar_Integrante(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        delegado = IntegrantesNucleo.objects.get(id=id_d)
        delegado.delete()
        return redirect('/listadoIntegrantes')


def editar_Integrante(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        temp = IntegrantesNucleo.objects.get(id=id_d)
        titulo = "Editar Integrante"
        if request.method == "POST":
            form = IntegrantesNucleoForm(request.POST, instance=temp)
            if form.is_valid():
                form.save()
            return redirect('/listadoIntegrantes')
        else:
            form = IntegrantesNucleoForm(instance=temp)
        return render(request, 'integrantes_nucleo/new.html', {'form': form, "titulo": titulo})


def eliminar_Jefe(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        delegado = JefeNucleo.objects.get(id=id_d)
        delegado.delete()
        return redirect('/listadoJefeN')


def editar_Jefe(request, id_d):
    if not request.user.is_authenticated():
        return redirect('/accounts/login')
    else:
        temp = JefeNucleo.objects.get(id=id_d)
        titulo = "Editar Jefe"
        if request.method == "POST":
            form = JefeNucleoForm(request.POST, instance=temp)
            if form.is_valid():
                form.save()
            return redirect('/listadoJefeN')
        else:
            form = JefeNucleoForm(instance=temp)
        return render(request, 'jefenucleo/new.html', {'form': form, "titulo": titulo})


# Registrar Usuario

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            user.save()
            return redirect('/')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro_usuario.html', {'form': form})


#	login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/library/libros")
    else:
        # Show an error page
        return HttpResponseRedirect("/accounts/login")


# logout

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/login")
