# Generated by Django 3.2.11 on 2022-02-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placemodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='imgs/'),
        ),
    ]
