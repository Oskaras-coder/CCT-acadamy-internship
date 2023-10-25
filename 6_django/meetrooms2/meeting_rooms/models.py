from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=255, unique=True)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50, null=False)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation_start = models.DateTimeField()
    reservation_end = models.DateTimeField()

    def __str__(self):
        return f'{self.employee} reserved {self.room} on {self.reservation_start} till {self.reservation_end} '