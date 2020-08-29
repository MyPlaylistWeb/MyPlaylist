# Generated by Django 3.0.8 on 2020-08-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='albumArt',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='albumArt/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='bugsUid',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='floUid',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='genieUid',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='melonUid',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='viveUid',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
