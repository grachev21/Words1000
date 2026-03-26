from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import WordsUser

from settings.models import WordsSettings

from .serializers import AllWordsSerializer, CardInfoSettingsSerializer


class AllWordsSet(viewsets.ReadOnlyModelViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AllWordsSerializer


class CardInfoiSettingsSet(viewsets.ReadOnlyModelViewSet):
    queryset = WordsSettings.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CardInfoSettingsSerializer


# class Home(ChartMixin, ServicesMixin, TemplateView):
#     template_name = "components/pages/home/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.init_data(
#             user=self.request.user,
#             check_user=self.request.user.is_anonymous,
#             context=context,
#         )


# class WordsPage(WordsMixin, LoginRequiredMixin, TemplateView):
#     template_name = "components/pages/words/words.html"
#     login_url = reverse_lazy("register")
#     paginate_by = 100

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         paginator = Paginator(self.filter["words_user"], self.paginate_by)
#         page_number = self.request.GET.get("page", 1)

#         try:
#             page_obj = paginator.page(page_number)
#         except PageNotAnInteger:
#             page_obj = paginator.page(1)
#         except EmptyPage:
#             page_obj = paginator.page(paginator.num_pages)

#         context["page_obj"] = page_obj
#         for obj in page_obj:
#             print(obj.core_words.word_en)
#         return context
