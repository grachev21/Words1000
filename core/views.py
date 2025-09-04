from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from core.services import ServicesMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import WordsUser
from core.services import WordsMixin
from .models import WordsCard


class Home(ServicesMixin, ListView):
    model = WordsCard
    template_name = "core/home.html"
    context_object_name = "words_counter_home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Вызываем метод init_data из миксина
        return self.init_data(user=self.request.user, check_user=self.request.user.is_anonymous, context=context)


class WordsPage(WordsMixin, LoginRequiredMixin, TemplateView):
    template_name = "core/words.html"
    login_url = reverse_lazy("register")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_data = self.filter(status=self.request.GET.get("status"), user=self.request.user)

        # Создаём Paginator
        paginator = Paginator(filter_data["words_user"], self.paginate_by)
        # Получаем номер страницы из GET-параметра
        page_number = self.request.GET.get("page", 1)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["page_obj"] = page_obj
        context["words_user"] = filter_data["words_user"]
        # Получаем STATUS_CHOICES из модели WordsUser, а не из QuerySet
        context["status_choices"] = WordsUser.STATUS_CHOICE
        context["current_status"] = filter_data["status_filter"]
        return self.init_data(user=self.request.user, context=context)

