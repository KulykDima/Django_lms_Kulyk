# Generated by Django 4.1.1 on 2022-09-20 16:53

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254, validators=[students.validators.valid_email_domains]),
            preserve_default=False,
        ),
    ]