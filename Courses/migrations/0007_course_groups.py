# Generated by Django 4.1.1 on 2022-10-14 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_group_course'),
        ('Courses', '0006_course_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='groups.group'),
        ),
    ]
