# Views

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm
from mixins.htmx_mixin import HtmxMixin


class LoginUser(HtmxMixin, LoginView):
    form_class = LoginUserForm
    template_name = "include_block.html"
    partial_template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Вход"
        return context

    def get_success_url(self):
        return reverse_lazy("core:home")


class RegisterUser(HtmxMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "include_block.html"
    partial_template_name = "users/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context

    def get_success_url(self):
        return reverse_lazy("login")


def logout_user(request):
    logout(request)
    return redirect("login")
