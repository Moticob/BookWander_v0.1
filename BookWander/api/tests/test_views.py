from django import setup
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils import timezone
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookWander.settings")
setup()
from api.models import User, Book, Order, OrderItem
from api.serializers import UserSerializer
# Tests for the views.


class TestUsersApi(APITestCase):
    """
    """

    def test_get_all_users(self):
        response = self.client.get("/api/v1/users/")
        users = User.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for u  in users:
            self.assertContains(response, u.user_id)

    def test_get_user(self):
        u = User.objects.all()[0]
        response = self.client.get(
            reverse("user_profile", kwargs={"id": u.user_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, u.user_id)

    def test_update_user(self):
        u = User.objects.filter(user_id=3).all()[0]
        u_data = {
            "username": "Robin_ohara",
            "email": "robinO@gmail.com",
            "password_hash":u.password_hash
        }
        response = self.client.put(
            reverse("user_profile", kwargs={"id": 3}),
            data=u_data,
            format="json"
        )
        u.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, u.user_id)
        self.assertEqual(u.username, u_data["username"])

    def test_delete_user(self):
        u = User.objects.all()[0]
        count = User.objects.count()
        response = self.client.delete(
            reverse("user_profile", kwargs={"id": u.user_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response_ch = self.client.get(
            reverse("user_profile", kwargs={"id": u.user_id}),
            format="json"
        )
        self.assertEqual(response_ch.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.count(), count - 1)

    def test_create_user(self):
        count = User.objects.count()
        u_data = {
            "username": "Nami_orange",
            "email": "namiO@gmail.com",
            "password_hash":"givememoney"
        }
        response = self.client.post(
            reverse("new_user"),
            u_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), count + 1)
        self.assertTrue(User.objects.filter(username="Nami_orange")[0])
        

class TestBooksApi(APITestCase):
    """
    tests the views of Book
    """

    def test_get_all_books(self):
        url = "/api/books/"
        response = self.client.get(url)
        books = Book.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for b  in books:
            self.assertContains(response, b.book_id)

    def test_get_book(self):
        books = Book.objects.all()[0]
        response = self.client.get(
            reverse(
                "book_detail",
                kwargs={"id": books.book_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, books.book_id)

    def test_update_book(self):
        book = Book.objects.filter(book_id=1).all()[0]
        b_data = {
            "genre": "Sci-Fi",
        }
        response = self.client.put(
            reverse(
                "book_detail",
                kwargs={"id": 1}),
            data=b_data,
            format="json"
        )
        book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, book.book_id)
        self.assertEqual(book.genre, b_data["genre"])

    def test_delete_book(self):
        u = Book.objects.all()[0]
        count = Book.objects.count()
        response = self.client.delete(
            reverse("book_detail", kwargs={"id": u.book_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response_ch = self.client.get(
            reverse("book_detail", kwargs={"id": u.book_id}),
            format="json"
        )
        self.assertEqual(response_ch.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Book.objects.count(), count - 1)

    def test_create_book(self):
        b_data = {
            "title": "Dune 2",
            "author": "Frank Herbert",
            "genre": "Science Fiction",
            "publication_date": "2001-01-08",
            "price": 100.00
        }
        count = Book.objects.count()
        response = self.client.post(
            reverse("new_book"),
            b_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(book_id=response.data["book_id"])[0])
        self.assertEqual(Book.objects.count(), count + 1)


class TestGenreApi(APITestCase):
    """"""

    def test_get_all_books(self):
        url = "/api/books/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
