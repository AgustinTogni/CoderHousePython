from django.shortcuts import render, redirect
from cuentas.forms import *
from django.db.models import Max
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def register(request):
    ultimo_numero = Perfiles.objects.aggregate(
        Max('numero_usuario')
    )['numero_usuario__max']

    numero_actual = (ultimo_numero or 0) + 1

    if request.method == "POST":
        form = PerfilesCreateForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.numero_usuario = numero_actual
            user.save()

            login(request, user)
            return redirect("productos:listar_productos")
    else:
        form = PerfilesCreateForm()

    return render(request, "cuentas/register.html", {
        "form": form
    })

@login_required
def visualiza_cuentas(request):
    return render(request, "cuentas/visualiza_cuentas.html", {"user": request.user})

@login_required
def actualiza_cuentas(request):
    if request.method == "POST":
        form = PerfilesChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("cuentas:visualiza_cuentas")
    else:
        form = PerfilesChangeForm(instance=request.user)
    
    return render(request, "cuentas/actualiza_cuentas.html", {"form": form})