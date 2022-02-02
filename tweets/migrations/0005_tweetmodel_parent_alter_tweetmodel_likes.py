# Generated by Django 4.0.1 on 2022-02-02 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_tweetlikemodel_remove_tweetmodel_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetmodel',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.tweetmodel'),
        ),
        migrations.AlterField(
            model_name='tweetmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_user', through='tweets.TweetLikeModel', to=settings.AUTH_USER_MODEL),
        ),
    ]
