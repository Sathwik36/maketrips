# Generated by Django 4.2.1 on 2023-08-21 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0018_alter_myreview_review_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myreview',
            name='review_time',
        ),
        migrations.AddField(
            model_name='myreview',
            name='rdate',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Date'),
        ),
    ]
