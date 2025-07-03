from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from users.models import WordsUser
from core.models import WordsCard


class WordsPage(LoginRequiredMixin, TemplateView):

    template_name = "words/words.html"
    login_url = reverse_lazy("register")
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        words_user = WordsUser.objects.filter(user=self.request.user).all()
        # context["words_user"] = words_user
        # Создаём Paginator
        paginator = Paginator(words_user, self.paginate_by)
        # Получаем номер страницы из GET-параметра
        page_number = self.request.GET.get("page", 1)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            # Если page не число, показываем первую страницу
            page_obj = paginator.page(1)
        except EmptyPage:
            # Если page вне диапазона (например, 9999), показываем последнюю
            page_obj = paginator.page(paginator.num_pages)

        context["page_obj"] = page_obj
        return context
    



