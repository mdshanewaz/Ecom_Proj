from django.db import models
from django.conf import settings

# Model
from Shop_App.models import ProductModel

# Create your models here.

class CartModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

# item1  quantity 3 price 150 total = 450
# item 2 quantity 1 price 400 total = 400 

class OrderModel(models.Model):
    orderitems = models.ManyToManyField(CartModel)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered =models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentID = models.CharField(max_length=264, blank=True, null=True)
    orderdID = models.CharField(max_length=200, blank=True, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems:
            total += float(order_item.get_total())
        return total