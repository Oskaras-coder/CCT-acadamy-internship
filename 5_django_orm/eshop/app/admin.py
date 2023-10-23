from django.contrib import admin
from django.urls import path, include

from app.models import Product, Address, Category, Cart, Product_Image, User, Cart_Product, Order, Order_Product

admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Product_Image)
admin.site.register(User)
admin.site.register(Cart_Product)
admin.site.register(Order)
admin.site.register(Order_Product)

