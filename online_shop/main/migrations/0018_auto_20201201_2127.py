# Generated by Django 3.1.3 on 2020-12-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_item_ref_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ref_num',
            field=models.TextField(unique=True),
        ),
    ]
