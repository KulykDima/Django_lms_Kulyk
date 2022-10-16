import django_filters
from django import forms
from django.db import models
from django_filters import FilterSet

from Courses.models import Course


class CreateCourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class EditCourse(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'


class GroupFilterSet(FilterSet):
    class Meta:
        model = Course
        fields = ['title']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }