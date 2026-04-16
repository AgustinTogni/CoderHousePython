from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from productos.models import Productos
from productos.forms import *
from django.urls import reverse_lazy
from django.db.models import Max
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProductosListView(LoginRequiredMixin, ListView):
    model = Productos
    template_name = "productos/lista_productos.html"
    context_object_name = "productos"
    paginate_by = 10

    def get_queryset(self):
        productos_q = self.request.GET.get("producto", "")

        if productos_q:
            return Productos.objects.filter(nombre__icontains=productos_q)
        return Productos.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos_q"] = self.request.GET.get("producto", "")
        return context

class ProductosDetailView(LoginRequiredMixin, DetailView):
    model = Productos
    template_name = "productos/visualiza_productos.html"
    context_object_name = "producto"

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"

class ProductosCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = "productos/crea_productos.html"
    success_url = reverse_lazy("productos:listar_productos")

    def form_valid(self, form):
        ultimo_numero = Productos.objects.aggregate(
            Max("numero_producto")
        )["numero_producto__max"]

        form.instance.numero_producto = (ultimo_numero or 0) + 1
        return super().form_valid(form)

class ProductosUpdateView(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ProductosUpdateForm
    template_name = "productos/actualiza_productos.html"
    context_object_name = "producto"
    success_url = reverse_lazy("productos:listar_productos")

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"

class ProductosDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = "productos/elimina_productos.html"
    context_object_name = "producto"
    success_url = reverse_lazy("productos:listar_productos")

    slug_field = "numero_producto"
    slug_url_kwarg = "numero_producto"