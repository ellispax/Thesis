# Generated by Django 4.1.5 on 2023-05-08 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='water_used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_amnt', models.FloatField()),
                ('date', models.DateField()),
                ('t1', models.TimeField()),
                ('t2', models.TimeField()),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wt_farm_name', to='home.farm')),
            ],
        ),
        migrations.CreateModel(
            name='measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('temp', models.FloatField()),
                ('pH', models.FloatField()),
                ('humidity', models.FloatField()),
                ('moisture', models.FloatField()),
                ('timeStamp', models.CharField(default='2023101000000', max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='an_farm_name', to='home.farm')),
            ],
        ),
    ]
