from django.shortcuts import render, redirect, get_object_or_404
from proveedores.models import Proveedores
from proveedores.forms import *
from django.core.paginator import Paginator
from django.db.models import Max
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listar_proveedores(request):
    proveedores_q = request.GET.get("negocio", "")

    if proveedores_q:
        proveedores_list = Proveedores.objects.filter(negocio__icontains=proveedores_q)
    else:
        proveedores_list = Proveedores.objects.all()

    paginator = Paginator(proveedores_list, 10)
    page_number = request.GET.get("page")
    proveedores = paginator.get_page(page_number)

    context = {
        "proveedores": proveedores,
        "proveedores_q": proveedores_q,
        "is_paginated": proveedores.has_other_pages(),
        "page_obj": proveedores,
    }

    return render(request, "proveedores/lista_proveedores.html", context)

@login_required
def visualizar_proveedores(request, numero_proveedor):
    proveedor = get_object_or_404(Proveedores, numero_proveedor=numero_proveedor)

    return render(request, "proveedores/visualiza_proveedores.html", {
        "proveedor": proveedor
    })

@login_required
def crear_proveedores(request):
    ultimo_numero = Proveedores.objects.aggregate(
        Max('numero_proveedor')
    )['numero_proveedor__max']

    numero_actual = (ultimo_numero or 0) + 1

    if request.method == "POST":
        form = ProveedoresForm(request.POST)

        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.numero_proveedor = numero_actual
            proveedor.save()
            return redirect("proveedores:listar_proveedores")

    else:
        form = ProveedoresForm()

    return render(request, "proveedores/crea_proveedores.html", {
        "form": form
    })

@login_required
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
        "form": form,
        "proveedor": proveedor
    })

@login_required
def eliminar_proveedores(request, numero_proveedor):
    proveedor = get_object_or_404(Proveedores, numero_proveedor=numero_proveedor)

    if request.method == "POST":
        proveedor.delete()
        return redirect("proveedores:listar_proveedores")

    return render(request, "proveedores/elimina_proveedores.html", {
        "proveedor": proveedor
    })