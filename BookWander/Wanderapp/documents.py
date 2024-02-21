from Wanderapp.models import Genre, Book
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class GenreDocument(Document):
    """ """
    class Index:
        name = "genres"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }
    class Django:
        model = Genre
        fields = [
            "id",
            "genre_name",
            "slug"
        ]


@registry.register_document
class BookDocument(Document):
    genre_name = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "genre_name": fields.TextField(),
        "slug": fields.TextField()
    })
    class Index:
        name = "books"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }
    class Django:
        model = Book
        fields = [
            "book_id",
            "slug",
            "title",
            "author",
            "price",
            "description",
            "cover_image_url",
            "publication_date"
        ]