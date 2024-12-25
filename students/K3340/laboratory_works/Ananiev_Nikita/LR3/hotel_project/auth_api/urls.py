from django.urls import path, re_path
from .views import *


app_name = "auth_api"

urlpatterns = [
    path("users/<int:id>/", UserAPIView.as_view(), name="get_client"),
    re_path("^users/(?P<id>\d+)/cleaners/(?P<date>\d{4}-\d{2}-\d{2})/$", UserRelatedCleanersListAPIView.as_view(), name="cleaners_by_client"),
    re_path("^users/(?P<id>\d+)/other_clients/(?P<from>\d{4}-\d{2}-\d{2})/(?P<to>\d{4}-\d{2}-\d{2})/$", ClientsByUserLivingPeriodListAPIView.as_view(), name="clients_by_user_living_period"),
    path("users/list/", UserListAPIView.as_view(), name="get_client_list"),
    path('users/<slug:from_town>/', ClientsFromTownListAPIView.as_view(), name='get_users_from_town'),
    path("users/<int:id>/update", UserUpdateAPIView.as_view(), name="update_client"),
]