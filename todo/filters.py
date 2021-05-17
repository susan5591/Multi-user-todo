import django_filters
from django_filters import CharFilter

from .models import *

class WorkFilter(django_filters.FilterSet):
    Title = CharFilter(field_name = 'title', lookup_expr = 'icontains')
    Job = CharFilter(field_name = 'task', lookup_expr = 'icontains')
    class Meta:
        model = TODO
        fields = '__all__'