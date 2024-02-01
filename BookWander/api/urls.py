from django.urls import path
from .views import UsersApi, UserApi, UserCreateApi
from .views import BookCreateApi, BookApi, BooksApi, GenreApi

"""
"""
urlpatterns = [
    path('api/v1/users/profile/', UserCreateApi.as_view(), name="new_user"),
    path('api/v1/users/profile/<int:id>', UserApi.as_view(), name="user_profile"),
    path('api/v1/users/', UsersApi.as_view()),
    path('api/books/', BooksApi.as_view()),
    path('api/book/<int:id>', BookApi.as_view(), name="book_detail"),
    path('api/book/', BookCreateApi.as_view(), name="new_book"),
    path('api/books/categories/', GenreApi.as_view(), name="genre_list"),
]