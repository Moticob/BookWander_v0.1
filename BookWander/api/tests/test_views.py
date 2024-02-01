from django import setup
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse
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
        response = self.client.get('/api/v1/users/')
        users = User.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for u  in users:
            self.assertContains(response, u.user_id)

    def test_get_user(self):
        u = User.objects.all()[0]
        response = self.client.get(
            reverse('user_profile', kwargs={'id': u.user_id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, u.user_id)
