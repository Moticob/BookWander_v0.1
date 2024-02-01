from django.urls import re_path, path
from .views import UsersApi, UserApi, UserCreateApi

 
urlpatterns = [
    path('api/v1/users/profile/', UserCreateApi.as_view()),
    path('api/v1/users/profile/<int:id>', UserApi.as_view(), name="user_profile"),
    path('api/v1/users/', UsersApi.as_view())
]