# Generated by Django 4.2.1 on 2023-08-21 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0014_alter_myreview_review_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myreview',
            name='review_time',
        ),
    ]
