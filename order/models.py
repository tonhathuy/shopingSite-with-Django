from django.db import models
from cart.models import OrderItem
from user.models import CustomerUser
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=0)

