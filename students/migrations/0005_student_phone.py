# Generated by Django 4.1.1 on 2022-09-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(db_column='phone', default='Отсутствует', max_length=20, verbose_name='phone'),
        ),
    ]
