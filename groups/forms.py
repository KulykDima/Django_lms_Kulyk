from django import forms

from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_description',
            'date_of_start',
        ]

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
        ]

        widgets = {
            'date_of_start': forms.DateInput(attrs={'type': 'date'})
        }
