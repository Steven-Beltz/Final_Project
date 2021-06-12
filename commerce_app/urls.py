from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.login_success),
    path('register',views.login_success),
    # path('edit_profile',views.edit_profile),
    # path('edit_ship_add',views.edit_ship_add),
    # path('edit_bill_add',views.edit_bill_add),
    # path('logout',views.log_out),
    path('seller/orders',views.seller_orders),
    path('seller/orders/show',views.seller_orders_show), #add /<int:order_id>
    #path('seller/order/<int:order_id>/edit_status',views.edit_status),
    path('seller/products',views.seller_products), #add /<int:product_id>
    path('seller/products/edit_add',views.seller_edit_add), #edit needs /<int:product_id>
    path('buyer/search',views.buyer_search),
    path('buyer/products/show',views.buyer_products_show), #add <int:product_id>
    path('buyer/cart',views.buyer_cart),
]