from django.db import transaction
from rest_framework import serializers, generics
from .models import Address, Category, Cart, Product_Image, Product, User, Cart_Product, Order, Order_Product


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ("total_price", "created_at", "updated_at")

    @transaction.atomic
    def create(self, validated_data: dict, **kwargs):
        user = validated_data["user_id"]
        cart_id = Cart.objects.filter(user=user.id).first()

        cart_products = Cart_Product.objects.filter(cart_id=cart_id)
        total_price = sum(cart_item.product_id.price * cart_item.quantity for cart_item in cart_products)

        validated_data["total_price"] = total_price
        order = Order.objects.create(**validated_data)

        return order


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = '__all__'


class AddToCartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        cart_id = int(self.context["cart_id"])
        product_id = int(self.validated_data.get("product_id"))
        quantity = self.validated_data.get("quantity")

        cart = Cart.objects.get(pk=cart_id)
        product = Product.objects.get(pk=product_id)

        cart_item = Cart_Product.objects.create(cart_id=cart, quantity=quantity, product_id=product)
        cart_item.save()
        return cart_item

    class Meta:
        model = Cart_Product
        fields = ["product_id", "quantity"]
