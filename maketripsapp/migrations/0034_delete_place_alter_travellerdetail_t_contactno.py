# Generated by Django 4.2.1 on 2023-09-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketripsapp', '0033_travellerdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='place',
        ),
        migrations.AlterField(
            model_name='travellerdetail',
            name='T_contactNo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
