from rest_framework import serializers
from .models import UserAccount
from booking_api.serializers import BookingSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    bookings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = UserAccount
        fields = ['email', 'firstname', 'lastname', 'phone', 'bookings']


class UserSerializerBookings(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    class Meta:
        model = UserAccount
        fields = ['email', 'firstname', 'lastname', 'phone', 'bookings']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['email', 'firstname', 'lastname', 'phone', 'birth_date', 'password']
