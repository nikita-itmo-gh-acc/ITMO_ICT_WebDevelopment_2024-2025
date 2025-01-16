from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from auth_api.serializers import CustomUserSerializer
from auth_api.models import UserAccount

from .serializers import *


class RoomAPIView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    lookup_field = 'id'
    queryset = Room.objects.all()


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomFreeListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.filter(is_occupied=False)
        return queryset


class RoomResidentsAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        start_date, end_date = self.kwargs['from'], self.kwargs['to']
        return UserAccount.objects.filter(bookings__check_in_time__gte=start_date, bookings__departure_time__lte=end_date)



class RoomUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RoomUpdateSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'
    queryset = Room.objects.all()


class RoomTypeListAPIView(generics.ListAPIView):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()
