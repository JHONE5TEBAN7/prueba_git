from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse


def home(request):
    return render(request, "inicio/home.html")


class RoleLoginView(LoginView):
    template_name = "inicio/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse("admin:index")
        return reverse("client_dashboard")


def register(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("admin:index")
        return redirect("client_dashboard")

    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("client_dashboard")

    return render(request, "inicio/register.html", {"form": form})


@login_required
def client_dashboard(request):
    if request.user.is_staff:
        return redirect("admin:index")
    return render(request, "inicio/client_dashboard.html")