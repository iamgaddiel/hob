# Generated by Django 3.2.4 on 2021-08-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_player_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='video_clip_link',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
