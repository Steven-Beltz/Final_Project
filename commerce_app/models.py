from django.db import models
import re

# class UserManager(models.Manager):

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Billing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    card = models.IntegerField()
    security = models.IntegerField()
    expiriation = models.DateField() #how to make (mm)/(year)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Shipping(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    quantity = models.IntegerField() #not sure if this is necessary?
    # image = models.ImageField()
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    #order_products
    #listing_products

STATUS_CHOICES = (
    ("pending" , "in process"),
    ("shipped" , "shipped"),
    ("cancelled" , "cancelled"),
)

class Order(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_price = models.IntegerField() #can this be a function?
    order_products = models.ManyToManyField(Product, related_name="order_products")
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)

class Listing(models.Model):
    inventory_count = models.IntegerField()
    sold_count = models.IntegerField()
    listing_products = models.ManyToManyField(Product, related_name="listing_products")
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)