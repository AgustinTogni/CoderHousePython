from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from productos.models import Productos
from productos.forms import *

# Create your views here.

class ProductosListView(ListView):
    model = Productos
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"

    def get_queryset(self):
        productos_q = self.request.GET.get("producto", "")

        if productos_q:
            return Productos.objects.filter(nombre__icontains=productos_q)
        return Productos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos_q"] = self.request.GET.get("producto", "")
        return context

class ProductosDetailView(DetailView):
    model = Productos
    template_name = "productos/visualiza_productos.html"
    context_object_name = "producto"

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"

class ProductosCreateView(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = "productos/crea_productos.html"
    success_url = reverse_lazy("productos:listar_productos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["numero_actual"] = Productos.objects.count() + 1
        return context

class ProductosUpdateView(UpdateView):
    model = Productos
    form_class = ProductosUpdateForm
    template_name = "productos/actualiza_productos.html"
    context_object_name = "producto"
    success_url = reverse_lazy("productos:listar_productos")

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"

class ProductosDeleteView(DeleteView):
    model = Productos
    template_name = "productos/elimina_productos.html"
    context_object_name = "producto"
    success_url = reverse_lazy("productos:listar_productos")

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"