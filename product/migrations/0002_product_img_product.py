# Generated by Django 3.0.3 on 2020-02-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_product',
            field=models.CharField(default='', max_length=256),
        ),
    ]
