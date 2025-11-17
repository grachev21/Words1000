# Views

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from users.forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy
from django.contrib import messages


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

def RegisterUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Аккаунт создан для {username}!")
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(request, "users/register.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login")
    
