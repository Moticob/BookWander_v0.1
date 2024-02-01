from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book
from .serializers import UserSerializer, BookSerializer, GenreSerializer
from django.http import Http404
from django.db.models import Count


class UsersApi(APIView): 
    """
        
    """
    sc = UserSerializer

    def get(self, request):
        users = User.objects.all()
        s = self.sc(users, many=True)
        #status=status.HTTP_200_OK
        return Response(s.data)

class UserApi(APIView):
    """
        
    """
    sc = UserSerializer
    def get(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.sc(user)
        return Response(s.data)
    def put(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.sc(instance=user,
                    data=request.data,
                    partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            user = User.objects.get(user_id=id)
        except User.DoesNotExist:
            raise Http404("Given query not found....")
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCreateApi(APIView):
    """
        
    """
    sc = UserSerializer
    def post(self, request):
        s = self.sc(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class BookCreateApi(APIView):
    bs = BookSerializer
    def post(self, request):
        s = self.bs(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class BookApi(APIView):

    bs = BookSerializer

    def get(self, request, id):
        try:
            book = Book.objects.get(book_id=id)
        except Book.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.bs(book)
        return Response(s.data)

    def put(self, request, id):
        try:
            book = Book.objects.get(book_id=id)
        except Book.DoesNotExist:
            raise Http404("Given query not found....")
        s = self.bs(instance=book, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            book = Book.objects.get(book_id=id)
        except Book.DoesNotExist:
            raise Http404("Given query not found....")
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BooksApi(APIView): 
    """
    """
    bs = BookSerializer
    def get(self, request):
        """
        gets all books.
        """
        books = Book.objects.all()
        s = self.bs(books, many=True)
        return Response(s.data)


class GenreApi(APIView): 
    """
    """
    def get(self, request):
        """gets all genres in books."""
        genres = (Book.objects.values(
            'genre').annotate(book_count=Count('book_id')).order_by())
        print(genres)
        s = GenreSerializer(genres, many=True)
        return Response(s.data)
