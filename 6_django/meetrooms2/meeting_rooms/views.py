from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer, ReservationSerializer, EmployeeSerializer
from .models import Room, Reservation, Employee
from datetime import datetime, timedelta

from django.utils import timezone


# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCreateView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomByDepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        # Modify this to filter rooms based on the department of an employee.
        # For example, you can filter rooms by the department.
        department = self.kwargs.get('department')
        return Room.objects.filter(reservation__employee__department=department)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ChooseReservationTime(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            start_datetime = serializer.validated_data['start_datetime']
            end_datetime = serializer.validated_data['end_datetime']

            # Check room availability
            available_rooms = Room.objects.filter(available=True)
            reserved_rooms = Reservation.objects.filter(
                reservation_start__lt=end_datetime,
                reservation_end__gt=start_datetime
            ).values_list('room_id', flat=True)

            available_rooms = available_rooms.exclude(id__in=reserved_rooms)
            available_room_names = [room.name for room in available_rooms]

            response_data = {
                'message': 'Available rooms for the selected time:',
                'available_rooms': available_room_names
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Handle GET request (show available rooms for the selected time) here

        # Retrieve the start_datetime and end_datetime from the request.
        start_datetime = request.GET.get('start_datetime')
        end_datetime = request.GET.get('end_datetime')

        # Check if start_datetime and end_datetime are provided.
        if not start_datetime or not end_datetime:
            return Response({'detail': 'Please provide start_datetime and end_datetime parameters.'}, status=400)

        # Now you can query the database to find available rooms for the selected time period.
        # You would need to implement the logic for checking room availability and getting the available rooms.

        # Example: Query the database for available rooms (you need to customize this).
        available_rooms = Room.objects.filter(
            # Your query to find available rooms based on start_datetime and end_datetime
        )

        # Serialize the available rooms and return them in the response.
        serializer = RoomSerializer(available_rooms, many=True)

        return Response(serializer.data, status=200)


class CreateReservationView(APIView):

    def post(self, request):
        room_id = request.data.get('room_id')
        start_datetime_str = request.data.get('start_datetime')
        end_datetime_str = request.data.get('end_datetime')

        if not start_datetime_str or not end_datetime_str:
            return Response({'detail': 'Please provide start_datetime and end_datetime parameters.'},
                            status=status.HTTP_400_BAD_REQUEST)

        start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M:%S')
        end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%dT%H:%M:%S')

        # Calculate the reservation duration
        reservation_duration = end_datetime - start_datetime

        # Check if the reservation duration is between 15 minutes and 3 hours
        min_duration = timedelta(minutes=15)
        max_duration = timedelta(hours=3)

        if not (min_duration <= reservation_duration <= max_duration):
            return Response({'detail': 'Reservation duration must be between 15 minutes and 3 hours.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Check room availability
        room = Room.objects.get(pk=room_id)
        conflicting_reservations = Reservation.objects.filter(
            room=room,
            reservation_start__lt=end_datetime,
            reservation_end__gt=start_datetime
        )
        if conflicting_reservations.exists():
            return Response({'detail': 'The room is not available for the selected time range.'},
                            status=status.HTTP_400_BAD_REQUEST)

        employee = Employee.objects.get(name="Oskaras")
        # Create the reservation
        reservation = Reservation(
            employee=employee,
            room=room,
            reservation_start=start_datetime,
            reservation_end=end_datetime
        )
        reservation.save()

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomDeleteView(APIView):
    def post(self, request):
        room_id = request.data.get('room_id')

        try:
            room = Room.objects.get(pk=room_id)
            room.delete()
            return Response({'message': 'Meeting room deleted successfully'}, status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({'error': 'Meeting room not found'}, status=status.HTTP_404_NOT_FOUND)


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('created_at')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
