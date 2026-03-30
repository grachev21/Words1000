from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from settings.models import WordsSettings
from users.models import WordsUser

from .serializers import AllWordsSerializer, CardInfoSettingsSerializer


class AllWordsSet(viewsets.ReadOnlyModelViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AllWordsSerializer


class CardInfoiSettingsSet(viewsets.ReadOnlyModelViewSet):
    queryset = WordsSettings.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CardInfoSettingsSerializer
