# Generated by Django 3.2.4 on 2021-07-09 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_playermentorship_footbal_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermentorship',
            name='publicity_academy',
            field=models.CharField(choices=[('player', 'player'), ('academy', 'academy')], default='player', max_length=10),
            preserve_default=False,
        ),
    ]