# Generated by Django 4.1.7 on 2023-02-28 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_user_img_avatar_alter_user_img_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='img_cover',
            new_name='cover_pic_url',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='img_avatar',
            new_name='profile_pic_url',
        ),
    ]