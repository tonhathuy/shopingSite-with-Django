from django.db import models
from product.models import Variation
from user.models import CustomerUser
# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
