from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from app.models import Product, Category, Product_Image  # Import your Product model
from app.serializers import ProductSerializer  # Import your Product serializer


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

        # Create some sample products for testing
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
        url = '/api/products/'  # Adjust the URL to match your project's URL structure

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data
        products = ProductSerializer(Product.objects.all(), many=True)

        # Assert that the response data matches the expected data
        self.assertEqual(response.data, products.data)
