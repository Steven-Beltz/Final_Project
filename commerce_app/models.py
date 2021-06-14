from typing_extensions import Required
from django.db import models
import re

class User_Manager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email invalid, try again."
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use."
        if len(postData['first_name']) < 2 :
            errors['first_name'] = "First Name must be larger than 2 characters."
        if str.isalpha(postData['first_name']) != True :
            errors['first_name'] = "First Name can only contain alpabet characters"
        if len(postData['last_name']) < 2 :
            errors['last_name'] = "Last Name must be larger than 2 characters."
        if str.isalpha(postData['last_name']) != True :
            errors['last_name'] = "Last Name can only contain alpabet characters"
        if len(postData['password']) < 8 :
            errors['password'] = "Password must be at least 8 characters long."
        if postData['password'] != postData['password_confirm']:
            errors['password'] = "Passwords do not match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    objects = User_Manager()
    # user_billing
    # user_shipping

class Billing(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    card = models.IntegerField(Required=True)
    security = models.IntegerField(Required=True)
    expiriation = models.DateField(Required=True) #how to make (mm)/(year)
    user_billing = models.ForeignKey(User, related_name="user_billing", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    objects = User_Manager()

class Shipping(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    user_shipping = models.ForeignKey(User, related_name="user_shipping", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    objects = User_Manager()

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    # product_category

class Image(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    # product_images

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) #not sure if this is necessary?
    image_main = models.CharField(max_length=255, null=False, blank=True)
    images = models.ManyToManyField(Image, related_name="product_images")
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