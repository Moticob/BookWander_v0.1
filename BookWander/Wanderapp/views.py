
import abc
from .models import Book, Genre
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .serializers import GenreSerializer, BookSerializer
from .documents import GenreDocument, BookDocument
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from elasticsearch_dsl import Q
from rest_framework import status


def homepage(request):
    """View for homepage"""
    all_genres = Genre.objects.all()
    if request.method == "POST":
        req = request.POST['searched']
        #all_books = Book.books.filter(title=req)
        #new_req = "search/books/" + req + "/"
        quzry = Q("multi_match", query=req,
                  fields=["slug", "title", "author", "genre_name", "description"],
                  fuzziness="auto")
        search = BookDocument.search().query(quzry)
        all_books = search.execute()
        return render(request, './Wanderapp/homepage.html', {'books':all_books, 'genres':all_genres, 'is_search':1})
    else:
        all_books = Book.books.all()
        return render(request, './Wanderapp/homepage.html', {'books':all_books, 'genres':all_genres, 'is_search':0})


# view for a specific book
def book_detail(request, slug):
    """provides the detail of a single book"""
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, './Wanderapp/books/detail.html', {'book':book}) 

# view for all books in a genre
#@login_required
def genre_list(request, genre_slug):
    """shows books by genre"""
    genre = get_object_or_404(Genre, slug=genre_slug)
    books = Book.books.filter(genre_name=genre)
    return render(request, './Wanderapp/books/genre.html', {"genre":genre, 'book': books})


def search_all(request):
    
    """
    all_genres = Genre.objects.all()
    if request.method == "POST":
        req = request.POST['searched']
        all_books = Book.books.filter(title=req)
        return render(request, './Wanderapp/homepage.html', {'books':all_books, 'genres':all_genres})
    else:
        return render(request, './Wanderapp/homepage.html', {'books':None, 'genres':all_genres})
    """
    return render(status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.books.all()
    
    
class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """"""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            s = self.document_class.search().query(q)
            r = s.execute()
            print(f"Found {r.hits.total.value} hit(s) for query: '{query}'")
            rslt = self.paginate_queryset(r, request, view=self)
            serializer = self.serializer_class(rslt, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchGenres(PaginatedElasticSearchAPIView):
    """fuzzy searches in genres names.
    """
    document_class = GenreDocument
    serializer_class = GenreSerializer

    def generate_q_expression(self, query):
        return Q("multi_match", query=query,
                fields=["genre_name"], fuzziness="auto")
        

class SearchBooks(PaginatedElasticSearchAPIView):
    """fuzzy searches in Books.
    """
    document_class = BookDocument
    serializer_class = BookSerializer

    def generate_q_expression(self, query):
        return Q("multi_match",
                 query=query,
                 fields=[
                     "slug", "title", "author",
                     "genre_name",
                     "description"], fuzziness="auto")
