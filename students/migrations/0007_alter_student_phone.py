# Generated by Django 4.1.1 on 2022-10-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, db_column='phone', default='Отсутствует', max_length=20, verbose_name='phone'),
        ),
    ]