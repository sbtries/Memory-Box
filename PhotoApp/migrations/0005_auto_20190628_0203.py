# Generated by Django 2.2.2 on 2019-06-28 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoApp', '0004_auto_20190628_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
