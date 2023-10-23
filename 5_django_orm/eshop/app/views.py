from django.shortcuts import render

from rest_framework import viewsets, status, generics
from rest_framework.generics import CreateAPIView

from app.models import Address, Category, Cart, Product, Product_Image, User, Cart_Product, Order, Order_Product
from app.serializers import (
    AddressSerializer, CategorySerializer, CartSerializer, ProductSerializer, ProductImageSerializer,
    UserSerializer, CartProductSerializer, OrderSerializer, OrderProductSerializer, AddToCartSerializer,


)

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_single_product(self, request, pk=None):
        try:
            product = self.queryset.get(pk=pk)
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = Product_Image.objects.all()
    serializer_class = ProductImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = Cart_Product.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        return Cart_Product.objects.filter(cart_id=self.kwargs["cart_id"])

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddToCartSerializer
        else:
            return CartProductSerializer

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_id"]}


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = Order_Product.objects.all()
    serializer_class = OrderProductSerializer

