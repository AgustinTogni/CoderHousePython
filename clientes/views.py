from django.shortcuts import render
from clientes.models import Clientes

# Create your views here.

def listar_clientes(request):
    clientes_q = Clientes.objects.all()
    context = {
        "clientes": clientes_q
    }
    return render(request, "clientes/lista_clientes.html", context)