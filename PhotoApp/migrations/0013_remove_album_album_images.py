# Generated by Django 2.2.3 on 2019-07-12 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoApp', '0012_auto_20190710_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_images',
        ),
    ]
