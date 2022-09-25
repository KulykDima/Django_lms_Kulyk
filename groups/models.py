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
        blank=True,
    )
    date_of_start = models.DateField(default=date.today, null=False, blank=True, validators=[validate_start_date])
