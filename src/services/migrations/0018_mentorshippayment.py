# Generated by Django 3.2.4 on 2021-08-02 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20210731_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorshipPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(editable=False, max_length=20, unique=True)),
                ('amount', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('ref', models.CharField(max_length=20)),
                ('transaction', models.CharField(max_length=20, unique=True)),
                ('txref', models.CharField(blank=True, max_length=20, unique=True)),
                ('status', models.CharField(max_length=10)),
                ('duration', models.CharField(choices=[('3 months', '3-months'), ('6 months', '6-months'), ('1 year', '1-year')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.playermentorship')),
            ],
        ),
    ]