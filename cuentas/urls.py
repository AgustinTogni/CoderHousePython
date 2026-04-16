from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from cuentas.views import *

app_name = "cuentas"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="cuentas/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="cuentas/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("perfil/", profile_detail, name="perfil_detail"),
    path("perfil/change", profile_change, name="perfil_change")
]