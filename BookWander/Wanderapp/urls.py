from django.urls import path

from . import views

app_name = 'Wanderapp'

urlpatterns = [
    # homepage path
    path('homepage/', views.homepage),
]