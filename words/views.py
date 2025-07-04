from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from users.models import WordsUser


class WordsPage(LoginRequiredMixin, TemplateView):
    template_name = "words/words.html"
    login_url = reverse_lazy("register")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем параметр фильтра из GET-запроса
        status_filter = self.request.GET.get('status')

        # Фильтруем слова для текущего пользователя
        words_user = WordsUser.objects.filter(user=self.request.user)
        
        if status_filter:
            words_user = words_user.filter(status=status_filter)

        # Создаём Paginator
        paginator = Paginator(words_user, self.paginate_by)
        # Получаем номер страницы из GET-параметра
        page_number = self.request.GET.get("page", 1)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["page_obj"] = page_obj
        context['words_user'] = words_user
        # Получаем STATUS_CHOICES из модели WordsUser, а не из QuerySet
        context['status_choices'] = WordsUser.STATUS_CHOICE
        context['current_status'] = status_filter
        return context