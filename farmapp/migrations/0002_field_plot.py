# Generated by Django 4.1.5 on 2023-01-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='plot',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
