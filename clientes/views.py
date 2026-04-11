from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Clientes
from clientes.forms import *
from django.core.paginator import Paginator
from django.db.models import Max

# Create your views here.

def listar_clientes(request):
    clientes_q = request.GET.get("negocio", "")

    if clientes_q:
        clientes_list = Clientes.objects.filter(negocio__icontains=clientes_q)
    else:
        clientes_list = Clientes.objects.all()

    paginator = Paginator(clientes_list, 10)
    page_number = request.GET.get("page")
    clientes = paginator.get_page(page_number)

    context = {
        "clientes": clientes,
        "clientes_q": clientes_q,
        "is_paginated": clientes.has_other_pages(),
        "page_obj": clientes,
    }

    return render(request, "clientes/lista_clientes.html", context)

def visualizar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    return render(request, "clientes/visualiza_clientes.html", {
        "cliente": cliente
    })

def crear_clientes(request):
    ultimo_numero = Clientes.objects.aggregate(
        Max('numero_negocio')
    )['numero_negocio__max']

    numero_actual = (ultimo_numero or 0) + 1

    if request.method == "POST":
        form = ClientesForm(request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.numero_negocio = numero_actual
            cliente.save()
            return redirect("clientes:listar_clientes")

    else:
        form = ClientesForm()

    return render(request, "clientes/crea_clientes.html", {
        "form": form
    })

def actualizar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    if request.method == "POST":
        form = ClientesUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes:listar_clientes")
    else:
        form = ClientesUpdateForm(instance=cliente)

    return render(request, "clientes/actualiza_clientes.html", {
        "form": form,
        "cliente": cliente
    })

def eliminar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    if request.method == "POST":
        cliente.delete()
        return redirect("clientes:listar_clientes")

    return render(request, "clientes/elimina_clientes.html", {
        "cliente": cliente
    })