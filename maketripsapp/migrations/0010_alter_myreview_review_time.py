# Generated by Django 4.2.1 on 2023-08-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0009_myreview_review_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myreview',
            name='review_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
