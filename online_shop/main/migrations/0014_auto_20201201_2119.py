# Generated by Django 3.1.3 on 2020-12-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201201_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
