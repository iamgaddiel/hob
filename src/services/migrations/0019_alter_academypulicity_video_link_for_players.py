# Generated by Django 3.2.4 on 2021-08-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_mentorshippayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academypulicity',
            name='video_link_for_players',
            field=models.CharField(default='', max_length=200),
        ),
    ]