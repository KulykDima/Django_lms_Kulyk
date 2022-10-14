from django.core.validators import MinLengthValidator
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=15,
        verbose_name='first name',
        db_column='first name',
        validators=[MinLengthValidator(3, 'you entered a name shorter than 3 characters')],
        blank=False,
    )
    last_name = models.CharField(
        max_length=15,
        verbose_name='last name',
        db_column='last name',
        blank=False,
        validators=[MinLengthValidator(3, 'you entered a last name shorter than 3 characters')],

    )
    phone = models.CharField(
        max_length=12,
        verbose_name='phone',
        db_column='phone',
        blank=False,
        null=True,
    )

    salary = models.PositiveIntegerField(default=10_000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.salary})'

    class Meta:
        db_table = 'teacher_table'
