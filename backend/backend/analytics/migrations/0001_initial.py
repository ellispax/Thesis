# Generated by Django 4.1.5 on 2023-01-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
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
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='an_farm_name', to='home.farm')),
            ],
        ),
    ]
