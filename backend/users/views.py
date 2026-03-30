from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import WordsFilter

from users.models import WordsUser

from .serializers import (
    ChartMonthSerializer,
    ChartWeekSerializer,
    ChartYearSerializer,
    ListWordSerializer,
    RemainderCardInfoSerializer,
)
from .services import ChartMonthMixin, ChartWeekMixin, ChartYearMixin


class RemainderCardInfoSet(viewsets.ViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = RemainderCardInfoSerializer(request.user)
        return Response(serializer.data)


class ChartWeekSet(ChartWeekMixin, viewsets.ViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        chart = self.get_week_data(user=request.user)
        serializer = ChartWeekSerializer(chart, many=True)
        return Response(serializer.data)


class ChartMonthSet(ChartMonthMixin, viewsets.ViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        chart = self.get_month_data(user=request.user)
        serializer = ChartMonthSerializer(chart, many=True)
        return Response(serializer.data)


class ChartYearSet(ChartYearMixin, viewsets.ViewSet):
    queryset = WordsUser.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        chart = self.get_year_data(user=request.user)
        serializer = ChartYearSerializer(chart, many=True)
        return Response(serializer.data)


class WordPagination(PageNumberPagination):
    page_size = 10  # по умолчанию
    page_size_query_param = "size"  # ?size=20 — клиент может менять размер
    max_page_size = 100  # максимум
    page_query_param = "page"


class ListWordSet(viewsets.ModelViewSet):
    serializer_class = ListWordSerializer
    permission_class = [IsAuthenticated]
    queryset = WordsUser.objects.all()
    pagination_class = WordPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WordsFilter
