from datetime import date

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import Group
from .validators import valid_email_domains, ValidEmailDomain   # noqa
from .validators import validate_unique_email
VALID_DOMAIN_LIST = ('@gmail.com', '@yahoo.com')


class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        db_column='first_name_column',
        validators=[MinLengthValidator(2, '"first_name" field value less that two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        db_column='last_name_column',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less that two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)

    email = models.EmailField(validators=[validate_unique_email])
    # email = models.EmailField(validators=[ValidEmailDomain(*VALID_DOMAIN_LIST)])

    phone = models.CharField(
        default='Отсутствует',
        max_length=20,
        verbose_name='phone',
        db_column='phone',
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='students')

    def __str__(self):
        return f'{self.pk}: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'student_table'

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            birthday = f.date()
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email)
            try:

                st.full_clean()
                st.save()
            except ValueError:
                print('Incorrect data')
