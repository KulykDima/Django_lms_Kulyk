from django.core.exceptions import ValidationError

import students.models


def validate_unique_email(value):
    if students.models.Student.objects.filter(email=value).count() > 0:
        raise ValidationError(f'Email {value} is exists')
    return value
