# Generated by Django 5.0.7 on 2024-07-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
