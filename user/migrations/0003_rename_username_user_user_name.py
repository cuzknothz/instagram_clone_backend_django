# Generated by Django 4.1.7 on 2023-02-24 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_name',
        ),
    ]