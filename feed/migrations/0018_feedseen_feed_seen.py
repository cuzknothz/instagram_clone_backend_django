# Generated by Django 4.1.7 on 2023-03-02 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0017_alter_feed_caption_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedSeen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='seen',
            field=models.ManyToManyField(related_name='feed_seen', through='feed.FeedSeen', to=settings.AUTH_USER_MODEL),
        ),
    ]
