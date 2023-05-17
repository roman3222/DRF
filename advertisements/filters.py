import django_filters
from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    creator_id = filters.NumberFilter(field_name='creator_id')
    created_at_after = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte')
    status_adv = django_filters.CharFilter(field_name='status')

    class Meta:
        model = Advertisement
        fields = [
            'creator_id',
            'created_at_after',
            'created_at_before',
            'status_adv',
        ]
