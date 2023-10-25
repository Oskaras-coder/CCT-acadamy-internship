from django.contrib import admin
from .models import Employee, Reservation, Room

# Register your models here.

admin.register()

admin.site.register(Employee)
admin.site.register(Reservation)
admin.site.register(Room)