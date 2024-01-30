from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import *


def homepage(request):
    """View for homepage"""
    all_books = Book.objects.all()
    return render(request, './Wanderapp/homepage.html', {'books':all_books})


# view for a specific book
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, './Wanderapp/books/detail.html', {'book':book}) 

# view for all books in a genre
def genre_list(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    books = Book.objects.filter(genre_name=genre)
    return render(request, './Wanderapp/books/genre.html', {"genre":genre, 'book': books})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page

