from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.loginView.as_view(template_name='account/registration/login.html',
                                               form_class=UserLoginForm), name='login'),
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),

    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]