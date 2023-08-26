from django.urls import reverse

from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import CasoSerializer, ClienteSerializer, AbogadoSerializer
from .models import Caso, Cliente, Abogado
from .forms import CasoForm, AbogadoForm, ClienteForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'  # Cambia el nombre del contexto a algo más genérico

    def get_queryset(self):
        # Retorna una lista combinada de objetos de diferentes modelos
        data ={
            "caso":Caso.objects.all(),
            "cliente":Cliente.objects.all(),
            "abogado":Abogado.objects.all(),
            
        }
        return data

class CrearCasoView(CreateView):
    model = Caso
    form_class = CasoForm
    template_name = 'caso/caso.html'
     # Cambia esto a la URL deseada

    def form_valid(self, form):
        nombre = form.cleaned_data.get('nombre')
        nro_expediente = form.cleaned_data.get('nro_expediente')

    def get_success_url(self):
         return reverse("index")


class CrearClienteView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente.html'

    def form_invalid(self, form):
        nombre = form.cleaned_data.get('nombre')
        edad = form.cleaned_data.get('edad')
        telefono = form.cleaned_data.get('telefono')


    def get_success_url(self):
         return reverse("index")


class CrearAbogadoView(CreateView):
    model = Abogado
    form_class = AbogadoForm
    template_name = "abogado/abogado.html"

    def form_invalid(self, form):
        nombre = form.cleaned_data.get('nombre')
        edad = form.cleaned_data.get('edad')
        telefono = form.cleaned_data.get('telefono')
        
    def get_success_url(self):
         return reverse("index")
    


class AbogadoDetailView(DetailView):
    model = Abogado
    template_name = "abogado/abogado_details.html"
    context_object_name = 'abogado'  # Cambia el nombre del contexto a 'abogado'

    def get_queryset(self):
        return Abogado.objects.all()



#   VISTA DE LAS APIS

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer

    def create(self, request,*args, **kwargs):
        user = request.user
        if user.is_admin:
            return super().create(request,*args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class AbogadoViewSet(viewsets.ModelViewSet):
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerializer
