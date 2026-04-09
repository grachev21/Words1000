from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from settings.models import WordsSettings

from .serializers import SettingWordsGetSerializer, SettingWordsPutSerializer


class SettingsWordsSet(viewsets.ModelViewSet):
    queryset = WordsSettings.objects.all()
    serializer_class = SettingWordsGetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WordsSettings.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        method = self.request.method

        if method == "PUT":
            return SettingWordsPutSerializer
        elif method == "GET":
            return SettingWordsGetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class ResettingDictionaries(
#     SettingsReset, SettingsStatus, LoginRequiredMixin, FormView
# ):
#     template_name = "settings/resetting_dictionaries.html"
#     form_class = ResettingDictionariesForm
#     login_url = reverse_lazy("register")
#     success_url = reverse_lazy("home")

#     def setup(self, request, *args, **kwargs):
#         super().setup(request, *args, **kwargs)
#         self.setup_settings_reset(request.user)
#         self.setup_settings_status(request.user)

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["title"] = "Сброс словаря"
#         return context
