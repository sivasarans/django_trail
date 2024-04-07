from django.db import models

#class ConnectionStatus(models.Model):
    #status = models.CharField(max_length=200)

class Product(models.Model):
    product_name=models.CharField(max_length=200,null=True)
    product_code=models.CharField(max_length=200,null=True)
    price=models.FloatField(default=0)
    gst=models.IntegerField(default=0)
    food_product=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
        #return self.product_name + " || " + self.product_code

# tests.py# models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Supplier(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if slug is not set
            self.slug = slugify(self.name)  # Generate slug based on name if not set
        super().save(*args, **kwargs)  # Call the save method of the parent class
class Customer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
