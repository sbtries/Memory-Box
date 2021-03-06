# Generated by Django 2.2.3 on 2019-07-10 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoApp', '0010_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='description',
            new_name='album_description',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='title',
            new_name='album_title',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='year',
            new_name='album_year',
        ),
        migrations.RemoveField(
            model_name='album',
            name='images',
        ),
        migrations.AddField(
            model_name='album',
            name='album_images',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='post_images', to='PhotoApp.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_album', to='PhotoApp.Album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='app_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_album', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='app_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_app_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
