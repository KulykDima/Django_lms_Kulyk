import re

from django import forms

from .models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'email',
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

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value


class EditStudentForm(CreateStudentForm):
    class Meta(CreateStudentForm.Meta):
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]
