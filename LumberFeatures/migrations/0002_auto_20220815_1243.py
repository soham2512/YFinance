# Generated by Django 3.2 on 2022-08-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LumberFeatures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lumberdata',
            name='Dividends',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='lumberdata',
            name='Stock_Splits',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='lumberdata',
            name='Volume',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
