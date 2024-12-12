## Приложение hotel_api.
### Назначение: отвечает за запросы связанные с номерами отеля.

### models.py:
```python
from django.db import models
from django.utils import timezone


class Room(models.Model):
    number = models.CharField(unique=True, max_length=4)
    area = models.IntegerField(null=False)
    is_occupied = models.BooleanField(default=False)
    is_cleaned = models.BooleanField(default=True)
    floor = models.IntegerField(null=False)
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, null=False, related_name='rooms')

    class Meta:
        constraints = [models.CheckConstraint(condition=models.Q(number__regex=r'\d{3,4}'), name='number_constraint'),
                       models.CheckConstraint(condition=models.Q(floor__gte=0), name='floor_constraint'),]

    def __str__(self):
        return f"room {self.number}, {self.area} sq meters, is_occupied: {self.is_occupied}"

class RoomType(models.Model):
    name = models.CharField(unique=True, max_length=30, null=False)
    places = models.IntegerField(null=False)
    description = models.TextField()
    class Meta:
        constraints = [models.CheckConstraint(condition=models.Q(places__lte=4), name='places <= 4'),
                       models.CheckConstraint(condition=models.Q(places__gte=1), name='places >= 1')]

    def __str__(self):
        return "room type:" + self.name

class RoomTypePrice(models.Model):
    day_price = models.IntegerField(null=False)
    start_date = models.DateField(null=False, default=timezone.now)
    end_date = models.DateField()
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, null=False, related_name='prices')

    class Meta:
        constraints = [models.CheckConstraint(condition=models.Q(day_price__gt=0), name='price > 0'),]
```

### serializers.py:
```python
from rest_framework import serializers
from .models import Room, RoomType


class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['is_cleaned', 'is_occupied']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomDetailedSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()
    class Meta:
        model = Room
        fields = '__all__'
```

### urls.py:
```python
urlpatterns = [
    path('rooms/<int:id>/', RoomAPIView.as_view(), name='get_room'),
    path('rooms/<int:id>/update', RoomUpdateAPIView.as_view(), name='update_room'),
    path('rooms/list/', RoomListAPIView.as_view(), name='get_room_list'),
    path('rooms/room_types/', RoomTypeListAPIView.as_view(), name='get_room_type_list'),
]
```