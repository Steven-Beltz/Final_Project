from django.shortcuts import render, redirect
import bcrypt
from .models import *

def index(request):
    return render(request, "index.html")

def login_success(request):
    return render(request, "choice.html")

def seller_orders(request):
    return render(request, "seller_orders.html")

def seller_orders_show(request):
    return render(request, "seller_orders_show.html")

def seller_products(request):
    return render(request, "seller_products.html")

def seller_edit_add(request):
    return render(request, "seller_edit_add.html")

def buyer_search(request):
    return render(request, "buyer_search.html")

def buyer_products_show(request):
    return render(request, "buyer_products_show.html")

def buyer_cart(request):
    return render(request, "buyer_cart.html")