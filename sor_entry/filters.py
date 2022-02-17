from django_filters import FilterSet, DateFilter
from django.forms import DateInput 

from .models import SOREntry

# Filter class for querying sor codes 
class SORCodeFilter(FilterSet):
    
    class Meta: 
        
        model = SOREntry
        
        fields = ['date_created']
    
    # Date select widget 
    date_created = DateFilter(label='Date Created', lookup_expr='date', widget=DateInput(attrs={'type':'date'}))