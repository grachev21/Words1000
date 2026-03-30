import django_filters
from .models import WordsUser 

class WordsFilter(django_filters.FilterSet):
    # Фильтр по одному статусу
    status = django_filters.CharFilter(field_name='status')
    
    # Фильтр по нескольким статусам (самый частый кейс!)
    status__in = django_filters.BaseInFilter(
        field_name='status',
        lookup_expr='in'
    )

    class Meta:
        model = WordsUser
        fields = ['status', 'status__in']  # можно добавить другие поля