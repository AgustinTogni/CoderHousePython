from django.shortcuts import render, redirect
from proveedores.models import Proveedores
from proveedores.forms import ProveedoresForm

# Create your views here.

def listar_proveedores(request):
    proveedores_q = Proveedores.objects.all()
    context = {
        "proveedores": proveedores_q
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

def buscar_proveedores(request):

    proveedores_q = request.GET.get("negocio", "")

    if proveedores_q:
        proveedores = Proveedores.objects.filter(negocio__icontains=proveedores_q)
    else:
        proveedores = Proveedores.objects.all()

    return render(request, "proveedores/lista_proveedores.html", {
        "proveedores": proveedores,
        "proveedores_q": proveedores_q
    })