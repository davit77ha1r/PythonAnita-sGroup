# Generated by Django 3.1.3 on 2020-11-30 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_item_post_nominals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='post_nominals',
        ),
    ]