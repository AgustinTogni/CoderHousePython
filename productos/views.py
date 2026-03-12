from django.shortcuts import render
from productos.models import Productos

# Create your views here.

def listar_productos(request):
    productos_q = Productos.objects.all()
    context = {
        "productos": productos_q
    }
    return render(request, "productos/lista_productos.html", context)