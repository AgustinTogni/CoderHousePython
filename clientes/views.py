from django.shortcuts import render, redirect
from clientes.models import Clientes
from clientes.forms import ClientesForm

# Create your views here.

def listar_clientes(request):
    clientes_q = Clientes.objects.all()
    context = {
        "clientes": clientes_q
    }
    return render(request, "clientes/lista_clientes.html", context)

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

def buscar_clientes(request):

    clientes_q = request.GET.get("negocio", "")

    if clientes_q:
        clientes = Clientes.objects.filter(negocio__icontains=clientes_q)
    else:
        clientes = Clientes.objects.all()

    return render(request, "clientes/lista_clientes.html", {
        "clientes": clientes,
        "clientes_q": clientes_q
    })