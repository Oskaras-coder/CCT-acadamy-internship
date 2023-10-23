from django.db import models
import uuid
from decimal import Decimal

from django.utils import timezone


class Address(models.Model):  # DONE
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=100, null=False)  # null
    city = models.CharField(max_length=60, null=False)  # null
    country = models.CharField(max_length=100, null=False)  # null
    zip = models.IntegerField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Category(models.Model):  # Done
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)  # Null
    sort_order = models.IntegerField()
    parent_category_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Cart(models.Model):  # DONE
    cart_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def num_of_items(self):
    #     cart_items = self.cart_products.all()
    #     quantity_sum = sum([qty.quantity for qty in cart_items])
    #     return quantity_sum
    #
    # @property
    # def cart_total(self):
    #     cart_items = self.cart_products.all()
    #     qtysum = sum([qty.subTotal for qty in cart_items])
    #     return qtysum

    def __str__(self):
        return str(self.cart_id)


class Product_Image(models.Model):  # DONE
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_name = models.CharField(max_length=100, null=False)  # null
    url = models.CharField(max_length=255, null=False)  # null


class Product(models.Model):  # Done
    product_id = models.AutoField(primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False)  # null
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)  # null
    product_image_id = models.ForeignKey(Product_Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product name {self.name}"

    class DoesNotExist:
        pass


class User(models.Model):  # DONE
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=False)  # null
    last_name = models.CharField(max_length=100, null=False)  # null
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=255, null=True, help_text="Store hashed password")
    email = models.EmailField(max_length=255, null=False)  # null
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)
    cart_id = models.OneToOneField(Cart, default=None, on_delete=models.CASCADE, null=True)
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} email. Address id - {self.address_id}"


class Cart_Product(models.Model):  # Done
    quantity = models.IntegerField()
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_products")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_products")

    @property
    def subTotal(self):
        total = self.quantity * self.product_id.price
        return total


class Order(models.Model):  # Done
    order_number = models.AutoField(primary_key=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, null=False)  # Null
    created_at = models.DateTimeField(auto_now_add=True)
    billing_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='billing_orders')
    shipping_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='shipping_orders')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order number - {self.order_number}"

    # def calculate_total_price(self):
    #     cart_items = self.cart.cart_products.all()
    #     total_price = sum(cart_item.product_id.price * cart_item.quantity for cart_item in cart_items)
    #     return total_price
    #
    # def save(self, *args, **kwargs):
    #     self.total_price = self.calculate_total_price()
    #     super(Order, self).save(*args, **kwargs)
    #
#     det i endpointa serializer

class Order_Product(models.Model):  # Done
    product_price = models.DecimalField(decimal_places=2, max_digits=10, null=False)  # null
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
