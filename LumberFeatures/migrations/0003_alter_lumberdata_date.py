# Generated by Django 3.2 on 2022-08-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LumberFeatures', '0002_auto_20220815_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lumberdata',
            name='Date',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]