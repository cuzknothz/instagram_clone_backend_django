# Generated by Django 4.1.7 on 2023-03-11 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0022_commentreply_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sdafdsf', to='feed.comment'),
        ),
    ]
