# Generated by Django 4.2 on 2023-04-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='channel',
        ),
        migrations.AddField(
            model_name='channel',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='post', to='main.post'),
        ),
    ]
