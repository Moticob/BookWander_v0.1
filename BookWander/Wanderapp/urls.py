from django.urls import path
from . import views
from .views import GenreViewSet, BookViewSet, SearchGenres, SearchBooks
from django.urls import path, include
from rest_framework import routers


app_name = 'wanderapp'
router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"books", BookViewSet)

urlpatterns = [
    # homepage path
    path('', views.homepage, name='homepage'),
    path('<slug:slug>', views.book_detail, name='book_detail'),  # path to book detail
    path('shop/<slug:genre_slug>', views.genre_list, name='genre_list'),
    #api get book, genre
    path('api/', include(router.urls)),
    #api search in books and genres
    path("search/genres/<str:query>/", SearchGenres.as_view()),
    path("search/books/<str:query>/", SearchBooks.as_view()),
]
