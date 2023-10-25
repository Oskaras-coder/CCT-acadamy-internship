from rest_framework import serializers

from .models import Room, Reservation, Employee


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationSerializer(serializers.Serializer):
    room = serializers.CharField()
    reservation_start = serializers.DateTimeField()
    reservation_end = serializers.DateTimeField()



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
