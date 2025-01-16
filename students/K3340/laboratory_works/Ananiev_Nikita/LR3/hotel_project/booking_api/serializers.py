from rest_framework import serializers
from .models import Booking
from django.db.models import Q
import datetime
from hotel_api.serializers import RoomSerializer
from auth_api.nested_serializers import NestedUserSerializer


def check_booking(instance):
    print(instance.planned_begin_date)
    if instance.planned_begin_date > instance.planned_end_date:
        raise serializers.ValidationError({"message": "End date must be greater than start date"})
    if instance.planned_begin_date < datetime.date.today():
        raise serializers.ValidationError({"message": "Start date must be today or later"})


class BookingDetailedSerializer(serializers.ModelSerializer):
    client = NestedUserSerializer()
    room = RoomSerializer()
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['client', 'room', 'booking_date', 'planned_begin_date', 'planned_end_date', 'from_town']

    def create(self, validated_data):
        booking = Booking(**validated_data)
        check_booking(booking)
        room_bookings = Booking.objects.filter(
            Q(room__pk=booking.room.pk) & ~Q(planned_begin_date__gt=booking.planned_end_date) &
            ~Q(planned_end_date__lt=booking.planned_begin_date))
        if room_bookings.exists():
            raise serializers.ValidationError({"message": "This room has already been booked on this dates"})
        booking.payment_status = 'not paid'
        booking.state = 'booked'
        booking.save()
        return Booking(**validated_data)


class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['planned_begin_date', 'planned_end_date']

    def update(self, instance, validated_data):
        instance.planned_begin_date = validated_data.get('planned_begin_date')
        instance.planned_end_date = validated_data.get('planned_end_date')
        check_booking(instance)
        instance.save()
        return Booking(**validated_data)
