# Generated by Django 3.0.8 on 2020-08-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistApp', '0002_auto_20200829_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='time',
            field=models.DurationField(blank=True, default=None, null=True),
        ),
    ]
