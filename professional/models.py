from django.db import models
from myapp.models import *

class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_since = models.DateField(null=True)
    
    def __str__(self):
        return self.customer_name
from django.db import models

class Orders(models.Model):
    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product_reference = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20, null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

# base/models.py
from django.db import models
from django.contrib.auth.models import User


class Suggestion(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    short_text_field = models.TextField()
    brief_description = models.TextField()
    image = models.ImageField(upload_to='suggestion_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title

    
