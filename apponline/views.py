from tkinter import commondialog
from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apponline.models import Carteras
from apponline.forms import CarterasFormulario


def inicio(request):

      return render(request, "apponline/inicio.html")


def carteras(request):
      carteras = Carteras.objects.all()
      return render(request, "apponline/carteras.html", {'carteras': carteras})


def camperas(request):

      return render(request, "apponline/camperas.html")


def zapatos(request):

      return render(request, "apponline/zapatos.html")


def accesorios(request):

      return render(request, "apponline/accesorios.html")


# Formulario a mano
# def carteras_formulario(request):
#       if request.method == 'POST':
#             data_formulario: Dict = request.POST
#             carteras = carteras(nombre=data_formulario['nombre'], codigo=data_formulario['codigo'])
#             carteras.save()
#             return render(request, "apponline/inicio.html")
#       else:  # GET
#             return render(request, "apponline/form_carteras.html")


def carteras_formulario(request):
      if request.method == 'POST':
            formulario= CarterasFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  carteras = carteras(nombre=data['nombre'], codigo=data['codigo'])
                  carteras.save()
                  return render(request, "apponline/inicio.html", {"exitoso": True})
      else:  # GET
            formulario= CarterasFormulario()  # Formulario vacio para construir el html
      return render(request, "apponline/form_carteras.html", {"formulario": formulario})


def busqueda_carteras(request):
      return render(request, "apponline/form_busqueda_carteras.html")


def buscar(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            carteras = carteras.objects.filter(codigo__icontains=codigo)
            return render(request, "apponline/carteras.html", {'carteras': carteras})
      else:
            return render(request, "apponline/carteras.html", {'carteras': []})
