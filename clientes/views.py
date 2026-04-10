from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Clientes
from clientes.forms import *

# Create your views here.

def listar_clientes(request):
    clientes_q = request.GET.get("negocio", "")

    if clientes_q:
        clientes = Clientes.objects.filter(negocio__icontains=clientes_q)
    else:
        clientes = Clientes.objects.all()

    context = {
        "clientes": clientes,
        "clientes_q": clientes_q
    }

    return render(request, "clientes/lista_clientes.html", context)

def visualizar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    return render(request, "clientes/visualiza_clientes.html", {
        "cliente": cliente
    })

def crear_clientes(request):
    numero_actual = Clientes.objects.count() + 1

    if request.method == "POST":
        form = ClientesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("clientes:listar_clientes")

    else:
        form = ClientesForm()

    return render(request, "clientes/crea_clientes.html", {
        "form": form,
        "numero_actual": numero_actual
    })

def actualizar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    if request.method == "POST":
        form = ClienteUpdateForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes:listar_clientes")
    else:
        form = ClienteUpdateForm(instance=cliente)

    return render(request, "clientes/actualiza_clientes.html", {
        "form": form
    })

def eliminar_clientes(request, dni):
    cliente = get_object_or_404(Clientes, dni=dni)

    if request.method == "POST":
        cliente.delete()
        return redirect("clientes:listar_clientes")

    return render(request, "clientes/elimina_clientes.html", {
        "cliente": cliente
    })