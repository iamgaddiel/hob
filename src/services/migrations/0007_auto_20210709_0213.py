# Generated by Django 3.2.4 on 2021-07-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_rename_publicity_academy_playermentorship_publicity_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playermentorship',
            name='publicity_category',
        ),
        migrations.AddField(
            model_name='academypulicity',
            name='publicity_category',
            field=models.CharField(choices=[('player', 'player'), ('academy', 'academy')], default='', max_length=10),
            preserve_default=False,
        ),
    ]