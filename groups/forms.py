from django import forms
from django.db import models

import django_filters
from django_filters import FilterSet

from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'})
        }


class EditGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_description',
            'date_of_start',
            'headman'
        ]

        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'})
        }


class GroupFilterSet(FilterSet):
    class Meta:
        model = Group
        fields = ['group_name', 'date_of_start']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            models.DateField: {
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': forms.DateInput(attrs={'type': 'date'}),
                },
            },
        }
