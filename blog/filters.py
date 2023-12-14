from django_filters import FilterSet, DateFilter, CharFilter, NumberFilter
from django import forms

from blog.models import Blog


class BlogFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Title',
                       widget=forms.TextInput(attrs={'class': 'form-control'})
                       )
    start_views = NumberFilter(field_name='views', lookup_expr='gt', label='Start views',
                               widget=forms.NumberInput(attrs={'class': 'form-control'})
                               )
    end_views = NumberFilter(field_name='views', lookup_expr='lt', label='End views',
                             widget=forms.NumberInput(attrs={'class': 'form-control'})
                             )
    start_date = DateFilter(field_name='created', lookup_expr='gt', label='Start Date',
                            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                            )
    end_date = DateFilter(field_name='created', lookup_expr='lt', label='End Date',
                            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                            )
    class Meta:
        model = Blog
        fields = ['title', 'start_date', 'end_date', 'start_views', 'end_views']
