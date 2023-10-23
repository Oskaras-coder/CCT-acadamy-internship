from django.shortcuts import render

"""Task1"""
from django.utils import timezone

from app.models import User

one_month_ago = timezone.now() - timezone.timedelta(days=30)
users_last_month = User.objects.filter(created_at__gte=one_month_ago).order_by('-email')
for user in users_last_month:
    print(
        f'Email: {user.email}, First Name: {user.first_name}, Last Name: {user.last_name}, Created At: {user.created_at}')

"""Task2"""
from app.models import Order

top_10_orders = Order.objects.order_by('-total_price')[:10]
for order in top_10_orders:
    print(f'Order Number: {order.order_number}, Total Price: {order.total_price}, Created At: {order.created_at}')

"""Task3"""

from app.models import Order
from django.db.models import Sum
from django.utils import timezone

today = timezone.now()
first_day_of_current_month = today.replace(day=1)
first_day_of_previous_month = first_day_of_current_month - timezone.timedelta(days=1)
last_day_of_previous_month = first_day_of_current_month - timezone.timedelta(days=first_day_of_current_month.day)

total_sum = \
    Order.objects.filter(created_at__gte=first_day_of_previous_month,
                         created_at__lte=last_day_of_previous_month).aggregate(
        Sum('total_price'))['total_price__sum']

print(f'Total Sum of Previous Month\'s Orders: {total_sum}')

"""Task4"""

from app.models import User

user_ids = User.objects.values_list('id', flat=True)

for user_id in user_ids:
    print(user_id)

user_id = '24c9791f-92fb-43e2-ad78-2287ee4bab4f'  # Replace with the actual user ID
user = User.objects.select_related('address_id', 'cart_id').get(id=user_id)

user_orders = user.order_set.all().order_by('-created_at')

for order in user_orders:
    print(f"Order Number: {order.order_number}")
    print(f"Total Price: {order.total_price}")
    print(f"Created At: {order.created_at}")
    print("-" * 30)
