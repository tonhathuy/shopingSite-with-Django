# Generated by Django 3.0.3 on 2020-03-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200306_2148'),
        ('order', '0002_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='cart.OrderItem'),
        ),
    ]