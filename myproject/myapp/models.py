from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_level = models.CharField(max_length=50)
    user_status = models.CharField(max_length=50)
    user_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    product_name = models.CharField(max_length=200)
    order_number = models.CharField(max_length=100, unique=True)
    merchant_number = models.CharField(max_length=100)
    purchase_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number
