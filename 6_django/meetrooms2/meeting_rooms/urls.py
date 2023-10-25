from django.urls import path, include
from .views import (RoomCreateView, ReservationViewSet, RoomByDepartmentViewSet, ChooseReservationTime, CreateReservationView,
                    RoomDeleteView, EmployeeViewSet, RoomViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'rooms/(?P<department>[-\w]+)/by-department', RoomByDepartmentViewSet, basename='rooms-by-department')
router.register(r'users', EmployeeViewSet),
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rooms/create/', RoomCreateView.as_view(), name='create-room'),
    path('choose-reservation-time/', ChooseReservationTime.as_view(), name='available-rooms'),
    path('create-reservation/', CreateReservationView.as_view(), name='create-reservation'),
    path('rooms/delete-room/', RoomDeleteView.as_view(), name='delete-room'),
]