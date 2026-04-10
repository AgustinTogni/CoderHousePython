from django.shortcuts import render, redirect
from productos.models import Productos
from productos.forms import ProductosForm

# Create your views here.

def listar_productos(request):
    productos_q = request.GET.get("producto", "")

    if productos_q:
        productos = Productos.objects.filter(nombre__icontains=productos_q)
    else:
        productos = Productos.objects.all()

    context = {
        "productos": productos,
        "productos_q": productos_q
    }

    return render(request, "productos/lista_productos.html", context)

def crear_productos(request):
    numero_actual = Productos.objects.count() + 1

    if request.method == "POST":
        form = ProductosForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("productos:listar_productos")

    else:
        form = ProductosForm()

    return render(request, "productos/crea_productos.html", {
        "form": form,
        "numero_actual": numero_actual
    })