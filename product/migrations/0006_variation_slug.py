# Generated by Django 3.0.3 on 2020-03-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='slug',
            field=models.SlugField(default='test slug'),
            preserve_default=False,
        ),
    ]