# Generated by Django 4.2.1 on 2023-08-22 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0019_remove_myreview_review_time_myreview_rdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myreview',
            name='rdate',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
