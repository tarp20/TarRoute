# Generated by Django 3.1.5 on 2021-01-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_auto_20210119_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Number of Train')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Travel time')),
                ('city_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_from_set', to='cities.city', verbose_name='from which city')),
                ('city_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_to_set', to='cities.city', verbose_name='to which city')),
            ],
            options={
                'verbose_name': 'Train',
                'verbose_name_plural': 'Trains',
                'ordering': ['travel_time'],
            },
        ),
    ]
