from django.shortcuts import render
from proveedores.models import Proveedores

# Create your views here.

def listar_proveedores(request):
    proveedores_q = Proveedores.objects.all()
    context = {
        "proveedores": proveedores_q
    }
    return render(request, "proveedores/lista_proveedores.html", context)