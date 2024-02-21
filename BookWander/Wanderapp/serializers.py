from rest_framework import serializers
from .models import Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    """ Serializes the model genre """
    class Meta:
        model = Genre
        fields = "__all__"
        
class BookSerializer(serializers.ModelSerializer):
    """ Serializes the model book """
    genre_name = GenreSerializer()
    class Meta:
        model = Book
        fields = "__all__"
