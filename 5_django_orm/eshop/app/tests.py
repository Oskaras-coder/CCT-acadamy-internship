from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from app.models import Category, Product_Image, Cart, Cart_Product, Product, User, Order, Address, Order_Product
from app.serializers import ProductSerializer, AddToCartSerializer, OrderSerializer


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


class OrderSerializerTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            street="123 Main St",
            city="Test City",
            country="Test Country",
            zip=12345
        )
        self.category = Category.objects.create(
            name="Test Category",
            sort_order=1
        )
        self.product_image = Product_Image.objects.create(
            image_name="Product Image 1",
            url="http://example.com/image1.jpg"
        )
        self.product = Product.objects.create(
            price=10.00,
            name="Test Product",
            quantity=100,
            category_id=self.category,
            product_image_id=self.product_image
        )
        self.cart = Cart.objects.create()
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            phone="123-456-7890",
            password="hashed_password",
            email="john@example.com",
            cart_id=self.cart,  # Adjust as needed
            address_id=self.address
        )

        self.cart_product = Cart_Product.objects.create(
            quantity=2,
            cart_id=self.cart,
            product_id=self.product
        )
        self.order = Order.objects.create(
            total_price=0.00,
            billing_address_id=self.address,
            shipping_address_id=self.address,
            user_id=self.user
        )
        self.order_product = Order_Product.objects.create(
            product_price=10.00,  # Adjust as needed
            quantity=2,
            product_id=self.product,
            order_id=self.order
        )

    def test_create_order(self):
        # Add products to the user's cart
        cart_item1 = Cart_Product.objects.create(cart_id=self.cart, product_id=self.product, quantity=2)
        cart_item2 = Cart_Product.objects.create(cart_id=self.cart, product_id=self.product, quantity=4)

        # Prepare data for creating an order
        data = {
            "billing_address_id": self.address.address_id,
            "shipping_address_id": self.address.address_id,
            "user_id": self.user.id,
        }

        # Create an instance of the CreateOrderSerializer with the cart in the context
        serializer = OrderSerializer(data=data, context={"cart_id": self.cart.cart_id})

        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

        # Call the create method to create the order
        order = serializer.save()

        # Verify that an Order instance was created
        self.assertIsInstance(order, Order)

        # Verify that the order total price is correct (sum of products in the cart)
        expected_total_price = (self.product.price * cart_item1.quantity) + (self.product.price * cart_item2.quantity)
        self.assertEqual(order.total_price, expected_total_price)

        # # Verify that the cart is deleted
        # self.assertFalse(Cart.objects.filter(id=self.cart.id).exists())
        # self.assertFalse(Cart_Product.objects.filter(cart=self.cart).exists())
