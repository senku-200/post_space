# Generated by Django 4.2 on 2023-04-15 09:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_channel_post_post_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='dislikes',
            field=models.ManyToManyField(related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(related_name='post_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
