import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

#RELATIONSHIP BETWEEN CUSTOMER AND ORDER:
#The Customer model represents individuals who place orders.
#The Order model uses a ForeignKey to associate each order with a single customer (one-to-many relationship).
#on_delete=models.CASCADE ensures that if a customer is deleted, all their orders are also removed.
#related_name="orders" allows accessing orders of a customer using customer.orders.all().