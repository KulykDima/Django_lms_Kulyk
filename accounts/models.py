from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birthday = models.DateField(null=True, blank=True)

    city = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'profiles'

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years


# функция автоматически создает профиль для юзера
@receiver(post_save, sender=User)
def create_new_profile(sender, instance, created, **kwargs):
    if created:
        p = Profile(user=instance)
        p.save()
