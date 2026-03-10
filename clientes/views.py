from django.shortcuts import render
from clientes.models import Clientes

# Create your views here.

def listar_clientes(request):
    clientes_q = Clientes.objects.all()
    context = {
        "listar_clientes": clientes_q
    }
    return render(request, "clientes/lista_clientes.html", context)