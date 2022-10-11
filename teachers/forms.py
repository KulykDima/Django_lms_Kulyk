import re

from django import forms
from django_filters import FilterSet

from teachers.models import Teacher


class CreateTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone',
        ]

    def clean(self):
        pass

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        values = value.title()
        return values

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        values = value.title()
        return values

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        values = re.sub(r'[^0-9+\-()]', r'', value)
        return values


class EditTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'phone',
        ]

    def clean(self):
        pass

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        values = value.title()
        return values

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        values = value.title()
        return values

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        values = re.sub(r'[^0-9+\-()]', r'', value)
        return values


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
