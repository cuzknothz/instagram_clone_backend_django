# Generated by Django 4.1.7 on 2023-02-25 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_video_image_created_at_image_updated_at_feedvideo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='text',
            new_name='caption_text',
        ),
    ]