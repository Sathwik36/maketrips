# Generated by Django 4.2.1 on 2023-08-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0016_myreview_review_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myreview',
            name='review_time',
            field=models.DateField(default='2023-08-21 18:18:47'),
        ),
    ]
