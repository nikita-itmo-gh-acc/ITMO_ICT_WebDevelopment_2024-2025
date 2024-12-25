from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q
# from yaml import serialize

from .models import UserAccount
from .serializers import CustomUserSerializer, UserUpdateSerializer, UserSerializerBookings
from work_api.serializers import EmployeeSerializer
from work_api.models import WorkSchedule, Employee
from booking_api.models import Booking


class UserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializerBookings
    lookup_field = 'id'
    queryset = UserAccount.objects.all()


class UserListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserAccount.objects.all()


class ClientsFromTownListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        town = self.kwargs.get('from_town')
        return UserAccount.objects.filter(bookings__from_town=town)


class UserRelatedCleanersListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        date = self.kwargs['date']
        return Employee.objects.filter(Q(contracts__work_schedule__date=date) & Q(contracts__work_schedule__room__bookings__client__pk=self.kwargs['id']))


class ClientsByUserLivingPeriodListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        start_date, end_date = self.kwargs['from'], self.kwargs['to']
        client = UserAccount.objects.get(pk=self.kwargs['id'])
        client_booking = Booking.objects.filter(Q(client__pk=client.pk) & Q(check_in_time__lte=start_date) & Q(departure_time__gte=end_date))
        if client_booking.exists():
            return UserAccount.objects.exclude(Q(pk=client.pk) | Q(bookings__departure_time__lt=start_date) | Q(bookings__check_in_time__gt=end_date) | Q(bookings__check_in_time=None))
        return UserAccount.objects.none()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = 'id'
    queryset = UserAccount.objects.all()
