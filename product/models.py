from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    parent_ID = models.IntegerField(default=0)
    title = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    img_product = models.CharField(max_length=256, default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    price = models.IntegerField(default=0)
    sale_price = models.FloatField(blank=True, null=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

