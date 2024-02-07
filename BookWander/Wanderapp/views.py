from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    """View for homepage"""
    all_books = Book.books.all()
    return render(request, './Wanderapp/homepage.html', {'books':all_books})


# view for a specific book
def book_detail(request, slug):
    """provides the detail of a single book"""
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, './Wanderapp/books/detail.html', {'book':book}) 

# view for all books in a genre
@login_required
def genre_list(request, genre_slug):
    """shows books by genre"""
    genre = get_object_or_404(Genre, slug=genre_slug)
    books = Book.books.filter(genre_name=genre)
    return render(request, './Wanderapp/books/genre.html', {"genre":genre, 'book': books})
