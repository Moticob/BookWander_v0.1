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

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.username = validated_data.get('username', instance.username)
        instance.password_hash = make_password(validated_data.get('password_hash', instance.password_hash), hasher="bcrypt")
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance

    def validate_name(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Name already exist")
        return value


class BookSerializer(serializers.ModelSerializer):
    """ Serializes the model book """
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        book = Book.objects.create(
            title = validated_data["title"],
            author = validated_data["author"],
            genre = validated_data["genre"],
            publication_date = validated_data["publication_date"],
            price = validated_data["price"]
        )
        return book

    def update(self, instance, validated_data):
        instance.book_id = validated_data.get('book_id', instance.book_id)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.publication_date = validated_data.get(
            'publication_date',
            instance.publication_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
   genre = serializers.CharField(max_length=255)
   book_count = serializers.DecimalField(max_digits=10, decimal_places=0)
