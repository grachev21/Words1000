from rest_framework import serializers

from .models import WordsSettings


class SettingWordsGetSerializer(serializers.ModelSerializer):
    number_repetitions_display = serializers.SerializerMethodField()

    class Meta:
        model = WordsSettings
        fields = [
            "id",
            "max_number_read",
            "number_repetitions",
            "number_repetitions_display",
            "number_words",
            "number_write",
            "translation_list",
        ]

    def get_number_repetitions_display(self, obj):
        """Возвращает все варианты для number_repetitions"""
        return [
            {"key": key, "display": display}
            for key, display in WordsSettings.NUMBER_REPETITIONS_CHOICES
        ]


class SettingWordsPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsSettings
        fields = [
            "number_words",
            "number_repetitions",
            "number_write",
            "max_number_read",
            "translation_list",
        ]
        read_only_fields = ["user"]
