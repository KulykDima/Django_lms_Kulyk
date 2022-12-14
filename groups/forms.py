from django import forms
from django.db import models

import django_filters
from django_filters import FilterSet

from groups.models import Group


class CreateGroupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        from students.models import Student
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            Student.objects.select_related('group'),
            required=False)

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ['headman']

        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'})
        }


class EditGroup(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman_Group',
            required=False
        )
        self.fields['headman_field'].choices.insert(0, (0, '-------'))

    class Meta:
        model = Group
        fields = '__all__'
        exclude = [
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
