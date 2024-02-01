from rest_framework import serializers
from .models import User, Book, Order, OrderItem
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        """
        fields = ("user_id","username",
                  "email", "password_hash",
                  "registration_date", "updated_at")
        """
    def create(self, validated_data):
        validated_data["password_hash"] = make_password(validated_data["password_hash"], hasher="bcrypt")
        u = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password_hash=validated_data["password_hash"],
            registration_date=timezone.now()
        )
        return u