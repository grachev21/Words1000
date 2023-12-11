from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from ..models import *
from ..forms import *
from ..separate_logic.views_logic import DataMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from words.forms import RegisterUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from words.token import account_activation_token
from django.core.mail import EmailMessage


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'words/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        val = self.list_variables(title='Авторизация', user=self.request.user)
        return dict(list(context.items()) + list(val.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database 
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site 
            current_site = get_current_site(request)
            mail_subject = 'Ссылка для активации была отправлена на ваш адрес электронной почты.'
            message = render_to_string('words/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Пожалуйста зайдите на вашу почту и пройдите по ссылке') 
    else:
        form = RegisterUserForm()
    return render(request, 'words/register.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо за регистрацию, теперь вы можете зайти на сайт.')
    else:
        return HttpResponse('Activation link is invalid!')


def logout_user(request):
    logout(request)
    return redirect('login')
