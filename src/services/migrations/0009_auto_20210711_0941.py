# Generated by Django 3.2.4 on 2021-07-11 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_academypulicity_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicityPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('ref', models.CharField(max_length=20)),
                ('transaction', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('duration', models.CharField(choices=[('3 months', '3-months'), ('6 months', '6-months'), ('1 year', '1-year')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='PlayerPublicity',
        ),
        migrations.AddField(
            model_name='academypulicity',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='publicitypayment',
            name='academy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.academypulicity'),
        ),
    ]
