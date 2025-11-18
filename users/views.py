# Views

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "base.html"
    partial_template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Вход"
        return context

    def get_success_url(self):
        return reverse_lazy("home")

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            template_name = self.partial_template_name or self.template_name
            return TemplateResponse(self.request, template_name, context)
        else:
            return super().render_to_response(context, **response_kwargs)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "base.html"
    partial_template_name = "users/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context

    def get_success_url(self):
        return reverse_lazy("login")

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            template_name = self.partial_template_name or self.template_name
            return TemplateResponse(self.request, template_name, context)
        return super().render_to_response(context, **response_kwargs)


def logout_user(request):
    logout(request)
    return redirect("login")
