from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView

from inicio.views import RoleLoginView, client_dashboard, home, register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("cuenta/entrar/", RoleLoginView.as_view(), name="login"),
    path("cuenta/registro/", register, name="register"),
    path("cuenta/salir/", LogoutView.as_view(next_page="home"), name="logout"),
    path("cuenta/", client_dashboard, name="client_dashboard"),
]