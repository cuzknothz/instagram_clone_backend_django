# Generated by Django 4.1.7 on 2023-03-11 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0021_commentreply_alter_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='feed.comment'),
            preserve_default=False,
        ),
    ]