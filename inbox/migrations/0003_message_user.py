# Generated by Django 4.1.7 on 2023-03-05 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inbox', '0002_inbox_remove_message_recipient_remove_message_sender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message_inbox', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
