from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    """View for homepage"""
    return HttpResponse("Welcome to BookWander")
