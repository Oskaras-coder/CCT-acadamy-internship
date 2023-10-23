from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from app.models import Product, Category, Product_Image, Cart_Product, Cart
from app.serializers import ProductSerializer, AddToCartSerializer


class ProductAPITest(APITestCase):

    def setUp(self):
        category = Category.objects.create(name="Kitchen", sort_order=1)

        product_image1 = Product_Image.objects.create(
            image_name="product_image_1",
            url="image_url_1"
        )

        product_image2 = Product_Image.objects.create(
            image_name="product_image_2",
            url="image_url_2"
        )

        Product.objects.create(name="cup",
                               price=10.00,
                               quantity=100,
                               category_id=category,
                               product_image_id=product_image1)
        Product.objects.create(name="spoon",
                               price=20.00,
                               quantity=40,
                               category_id=category,
                               product_image_id=product_image2)

    def test_get_all_products(self):
        url = '/api/products/'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        products = ProductSerializer(Product.objects.all(), many=True)
        self.assertEqual(response.data, products.data)


class CartAPITest(APITestCase):
    def setUp(self):

        category = Category.objects.create(name="Kitchen", sort_order=1)

        product_image1 = Product_Image.objects.create(
            image_name="product_image_1",
            url="image_url_1"
        )

        product_image2 = Product_Image.objects.create(
            image_name="product_image_2",
            url="image_url_2"
        )
        # Create some sample products for testing
        self.product1 = Product.objects.create(name="cup", price=10.00, quantity=100, category_id=category,
                                               product_image_id=product_image1)
        self.product2 = Product.objects.create(name="spoon", price=20.00, quantity=40, category_id=category,
                                               product_image_id=product_image2)
        self.cart = Cart.objects.create()
        self.valid_data = {
            "product_id": self.product1.product_id,
            "quantity": 5,
        }

    def test_add_product_to_cart(self):
        # Create an instance of the serializer with context
        serializer = AddToCartSerializer(data=self.valid_data, context={"cart_id": self.cart.cart_id})

        # Check if the data is valid
        self.assertTrue(serializer.is_valid())

        # Call the create method to add the product to the cart
        cart_item = serializer.save()

        self.assertIsInstance(cart_item, Cart_Product)
        self.assertEqual(cart_item.product_id, self.product1)
        self.assertEqual(cart_item.quantity, 5)