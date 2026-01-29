from rest_framework import serializers


class GraphPointSerializer(serializers.Serializer):
    date_graph = serializers.CharField(allow_blank=True)
    count_graph = serializers.IntegerField()

class HomeSerializer(serializers.Serializer):
    week_data = GraphPointSerializer(many=True)
    month_data = GraphPointSerializer(many=True)
    year_data = GraphPointSerializer(many=True)
