from core.services import ServicesMixin
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import WordsCard
class Home(ServicesMixin, ListView):
    model = WordsCard
    template_name = "core/home.html"
    context_object_name = "words_counter_home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Вызываем метод init_data из миксина
        return self.init_data(user=self.request.user, check_user=self.request.user.is_active, context=context)


class ReadingSentences(LoginRequiredMixin, TemplateView):
    template_name = "core/reading_sentences.html"
    login_url = reverse_lazy("register")
