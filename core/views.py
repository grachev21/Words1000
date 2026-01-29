# Views
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.services.services import ServicesMixin, WordsMixin
from core.services.services_chart import ChartMixin
from mixins.htmx_mixin import HtmxMixin
from users.models import WordsUser

from .serializers import HomeSerializer

# class Home(ChartMixin, ServicesMixin, TemplateView):
#     template_name = "core/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.init_data(
#             user=self.request.user,
#             check_user=self.request.user.is_anonymous,
#             context=context,
#         )


class HomeApi(ChartMixin, ServicesMixin, GenericAPIView):
    serializer_class = HomeSerializer

    def get(self, request, *args, **kwargs):
            data = self.get_data_chart()

            serializer = HomeSerializer(data)
            return Response(serializer.data)

class WordsPage(WordsMixin, LoginRequiredMixin, TemplateView):
    template_name = "core/words.html"
    login_url = reverse_lazy("register")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_data = self.filter(
            status=self.request.GET.get("status"), user=self.request.user
        )

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
        context["status_choices"] = WordsUser.status
        context["current_status"] = filter_data["status_filter"]
        return self.init_data(user=self.request.user, context=context)
