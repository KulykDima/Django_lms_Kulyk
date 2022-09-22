from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    today = date.today()
    if today > value:
        raise ValidationError(f'Time {value} its past tense')
    return value
