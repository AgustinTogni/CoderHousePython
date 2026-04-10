from django.shortcuts import render, redirect, get_object_or_404
from proveedores.models import Proveedores
from proveedores.forms import *

# Create your views here.

def listar_proveedores(request):
    proveedores_q = request.GET.get("negocio", "")

    if proveedores_q:
        proveedores = Proveedores.objects.filter(negocio__icontains=proveedores_q)
    else:
        proveedores = Proveedores.objects.all()

    context = {
        "proveedores": proveedores,
        "proveedores_q": proveedores_q
    }

    return render(request, "proveedores/lista_proveedores.html", context)

def crear_proveedores(request):
    numero_actual = Proveedores.objects.count() + 1

    if request.method == "POST":
        form = ProveedoresForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("proveedores:listar_proveedores")

    else:
        form = ProveedoresForm()

    return render(request, "proveedores/crea_proveedores.html", {
        "form": form,
        "numero_actual": numero_actual
    })

def actualizar_proveedores(request, numero_proveedor):
    proveedor = get_object_or_404(Proveedores, numero_proveedor=numero_proveedor)

    if request.method == "POST":
        form = ProveedoresUpdateForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect("proveedores:listar_proveedores")
    else:
        form = ProveedoresUpdateForm(instance=proveedor)

    return render(request, "proveedores/actualiza_proveedores.html", {
        "form": form
    })