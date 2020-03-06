from django.contrib import admin
from .models import OrderItem, CustomerUser
# Register your models here.


admin.site.register(OrderItem)
admin.site.register(CustomerUser)