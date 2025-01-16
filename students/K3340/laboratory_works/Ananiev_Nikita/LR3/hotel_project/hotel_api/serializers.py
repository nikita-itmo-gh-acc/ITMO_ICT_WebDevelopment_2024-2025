from rest_framework import serializers
from .models import Room, RoomType, RoomTypePrice


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['is_cleaned', 'is_occupied']


class RoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypePrice
        fields = ['day_price']


class RoomTypeSerializer(serializers.ModelSerializer):
    prices = RoomPriceSerializer(read_only=True, many=True)
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    class Meta:
        model = Room
        fields = '__all__'


# class RoomDetailedSerializer(serializers.ModelSerializer):
#     room_type = RoomTypeSerializer()
#     class Meta:
#         model = Room
#         fields = '__all__'
