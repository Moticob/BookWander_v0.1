"""
creates views.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from .models import User, Book, Order, OrderItem

