# Generated by Django 4.1.5 on 2023-05-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='notification',
            field=models.TextField(null=True),
        ),
    ]
