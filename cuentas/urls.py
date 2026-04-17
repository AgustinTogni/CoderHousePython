from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from cuentas.views import *

app_name = "cuentas"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="cuentas/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="cuentas/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("perfil/", visualiza_cuentas, name="visualiza_cuentas"),
    path("perfil/actualizar", actualiza_cuentas, name="actualiza_cuentas")
]