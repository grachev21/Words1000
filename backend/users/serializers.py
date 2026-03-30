from core.models import WordsCard
from django.utils import timezone
from rest_framework import serializers

from users.models import WordsUser


class RemainderCardInfoSerializer(serializers.Serializer):
    remainder_day = serializers.SerializerMethodField()
    remainder_all = serializers.SerializerMethodField()
    unknown = serializers.SerializerMethodField()
    learning = serializers.SerializerMethodField()
    repetition = serializers.SerializerMethodField()
    learned = serializers.SerializerMethodField()

    def get_remainder_day(self, obj):
        return WordsUser.objects.filter(
            user=obj, status="4", created_at__date=timezone.now().date()
        ).count()

    def get_remainder_all(self, obj):
        return WordsUser.objects.filter(user=obj).count()

    def get_unknown(self, obj):
        return WordsUser.objects.filter(user=obj, status="1").count()

    def get_learning(self, obj):
        return WordsUser.objects.filter(user=obj, status="2").count()

    def get_repetition(self, obj):
        return WordsUser.objects.filter(user=obj, status="3").count()

    def get_learned(self, obj):
        return WordsUser.objects.filter(user=obj, status="4").count()


class ChartWeekSerializer(serializers.Serializer):
    date_graph = serializers.CharField()
    count_graph = serializers.IntegerField()


class ChartMonthSerializer(serializers.Serializer):
    date_graph = serializers.CharField()
    count_graph = serializers.IntegerField()


class ChartYearSerializer(serializers.Serializer):
    date_graph = serializers.CharField()
    count_graph = serializers.IntegerField()


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsCard
        fields = "__all__"


class ListWordSerializer(serializers.ModelSerializer):
    core_words = WordsSerializer()
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = WordsUser
        fields = ["core_words", "created_at", "number_repetitions", "status"]
