# Generated by Django 3.2.11 on 2022-02-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20220207_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placemodel',
            name='images',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]