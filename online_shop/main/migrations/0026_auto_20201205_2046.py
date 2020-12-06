# Generated by Django 3.1.3 on 2020-12-05 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0025_orderitem_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order_item',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
