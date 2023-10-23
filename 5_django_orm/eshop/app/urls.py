from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import (
    AddressViewSet, CategoryViewSet, CartViewSet, ProductViewSet, ProductImageViewSet,
    UserViewSet, CartProductViewSet, OrderViewSet, OrderProductViewSet,
)

router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', CartViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_images', ProductImageViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_products', OrderProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('carts/<str:cart_id>/add/', CartProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart-add'),
    # path('api/orders/create', OrderViewSet.as_view({'post': 'create'}), name='create-order'),
    # path('user/orders/', UserOrdersViewSet.as_view({'get': 'list'}), name='user-orders'),
]

