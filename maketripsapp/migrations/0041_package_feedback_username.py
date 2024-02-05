# Generated by Django 4.2.5 on 2023-11-28 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maketripsapp', '0040_vacations'),
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=70)),
                ('p_cname', models.CharField(max_length=70)),
                ('p_img', models.CharField(max_length=150)),
                ('No_D', models.IntegerField()),
                ('No_N', models.IntegerField()),
                ('No_F', models.IntegerField()),
                ('No_H', models.IntegerField()),
                ('p_price', models.IntegerField()),
                ('Offer_type', models.CharField(max_length=50)),
                ('p_item1', models.CharField(max_length=50)),
                ('p_item2', models.CharField(max_length=50)),
                ('p_item3', models.CharField(max_length=50)),
                ('p_item4', models.CharField(max_length=50)),
                ('p_item5', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
