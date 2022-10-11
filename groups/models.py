from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group name',
        validators=[MinLengthValidator(2, 'Group Name less than two symbols')]
    )
    group_description = models.TextField(
        max_length=150,
        verbose_name='Описание группы',
        blank=True
    )
    date_of_start = models.DateField(default=date.today, null=False, blank=True, validators=[validate_start_date])

    end_date = models.DateField(null=True, blank=True)

    headman = models.OneToOneField('students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')

    def __str__(self):
        return f'Group name: {self.group_name}'
