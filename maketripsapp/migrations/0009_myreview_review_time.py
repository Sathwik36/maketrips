# Generated by Django 4.2.1 on 2023-08-19 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0008_alter_myreview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='myreview',
            name='review_time',
            field=models.DateField(default=datetime.datetime(2023, 8, 19, 14, 39, 16, 918131)),
        ),
    ]
