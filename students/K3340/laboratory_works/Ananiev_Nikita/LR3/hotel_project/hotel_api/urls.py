from django.urls import path, re_path
from .views import *


app_name = "hotel_api"

urlpatterns = [
    path('rooms/<int:id>/', RoomAPIView.as_view(), name='get_room'),
    path('rooms/<int:id>/update', RoomUpdateAPIView.as_view(), name='update_room'),
    re_path('^rooms/(?P<id>\d+)/users/(?P<from>\d{4}-\d{2}-\d{2})/(?P<to>\d{4}-\d{2}-\d{2})/$', RoomResidentsAPIView.as_view(), name='get_residents_by_period'),
    path('rooms/list/', RoomListAPIView.as_view(), name='get_room_list'),
    path('rooms/free/', RoomFreeListAPIView.as_view(), name='get_free_rooms'),
    path('rooms/room_types/', RoomTypeListAPIView.as_view(), name='get_room_type_list'),
]