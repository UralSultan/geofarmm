# Generated by Django 4.1.5 on 2023-01-25 22:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Культура',
                'verbose_name_plural': 'Культуры',
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Фермер',
                'verbose_name_plural': 'Фермеры',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'Сезоны',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('plot', models.CharField(max_length=50, null=True, verbose_name='Поле')),
                ('culture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmapp.culture', verbose_name='Культура')),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmapp.farmer', verbose_name='Фермер')),
                ('seasons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmapp.season', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Поле',
                'verbose_name_plural': 'Поля',
            },
        ),
    ]
