from django.urls import path

from . import views

app_name = 'wanderapp'

urlpatterns = [
    # homepage path
    path('', views.homepage, name='homepage'),
    path('<slug:slug>', views.book_detail, name='book_detail'),  # path to book detail
    path('shop/<slug:genre_slug>', views.genre_list, name='genre_list'),
]
