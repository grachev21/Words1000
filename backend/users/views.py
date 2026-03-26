from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import RemainderCardInfoSerializer, ChartWeekSerializer, ChartMonthSerializer, ChartYearSerializer
from .services import ChartWeekMixin, ChartMonthMixin, ChartYearMixin
from users.models import WordsUser

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