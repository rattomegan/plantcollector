# Generated by Django 3.2.9 on 2022-01-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_care_feeding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeding',
            name='instructions',
        ),
        migrations.AddField(
            model_name='care',
            name='instructions',
            field=models.TextField(default='Feed every two weeks in growing season', max_length=400),
        ),
    ]
