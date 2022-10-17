from django.db import models

from groups.models import Group


class Course(models.Model):
    title = models.CharField(max_length=15, null=False, blank=True)

    price = models.IntegerField(null=True, blank=True)

    lessons = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title
