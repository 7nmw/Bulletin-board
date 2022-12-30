from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Responses
import django_filters



class ResponsesFilter(FilterSet):
    class Meta:
        model = Responses
        fields = {
            'text_responses': ['icontains'],
            'user_responses': ['exact'],
            'accepted': ['exact'],
        }