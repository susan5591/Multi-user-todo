# Generated by Django 3.0.8 on 2021-05-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210517_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(1, '1️'), (2, '2️'), (3, '3️'), (4, '4️'), (5, '5️'), (6, '6️'), (7, '7️'), (8, '8️'), (9, '9️'), (10, '10')], max_length=2),
        ),
    ]
