from rest_framework import serializers
from settings.models import WordsSettings
from users.models import WordsUser

from core.models import WordsCard


class AllWordsSerializer(serializers.ModelSerializer):
    word = serializers.CharField(source="core_words")

    class Meta:
        model = WordsUser
        fields = ["status", "word"]


class CardInfoSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsSettings
        fields = [
            "number_words",
            "number_repetitions",
            "number_write",
            "max_number_read",
            "translation_list",
        ]
