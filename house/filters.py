from .models import House, City, Bedroom, Floor, Area, Direction
import django_filters
from django.db.models import Q


# Filter house by city, bedroom number, floor and area
class HouseFilter(django_filters.FilterSet):
    '''
    根据城市，房型，面积，楼层和朝向筛选二手房
    '''
    # q = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label="Keywords")
    q = django_filters.CharFilter(method='my_custom_filter')
    city = django_filters.ChoiceFilter(field_name='community__city', choices=City.choices,
                                         label='城市')
    bedroom = django_filters.ChoiceFilter(field_name='bedroom', choices=Bedroom.choices,
                                         label='房型')
    area = django_filters.ChoiceFilter(field_name='area_class', choices=Area.choices,
                                         label='面积')
    floor = django_filters.ChoiceFilter(field_name='floor', choices=Floor.choices,
                                         label='楼层')
    direction = django_filters.ChoiceFilter(field_name='direction', choices=Direction.choices,
                                        label='楼层')


    def my_custom_filter(self, queryset, q, value):
        return queryset.filter(Q(description__icontains=value) | Q(community__name__icontains=value))


    class Meta:
        model = House
        fields = {
            # 'title': ['icontains'],
            # 'category__name': ['icontains'],
            # 'pub_date': ['date__gte'],
        }

