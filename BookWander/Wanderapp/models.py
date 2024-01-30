from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

# Create your models here.


# Users Table
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password_hash = models.CharField(max_length=255)
    registration_date = models.DateTimeField()

    def __str__(self):
        return f'{self.username}'
# Genre table
class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('wanderapp:genre_list', args=[self.slug])

    def __str__(self):
        return f"{self.genre_name}"

# Books Table
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image_url = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('wanderapp:book_detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} {self.genre_name} {self.author}"

# Orders Table
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order_id} {self.user_id}"

# Order_Items Table
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_title")
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order_item_id} {self.order_id} {self.book_id}"

# User_Preferences Table
class UserPreferences(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)
    preferred_authors = models.CharField(max_length=255)
    notification_settings = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user_id} {self.favorite_genre} {self.preferred_authors}"

# Reviews Table
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(MaxValueValidator(5))
    comment = models.TextField()
    review_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_id} {self.book_id} rating:{self.rating} {self.comment}"

# Feedback Table
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    feedback_date = models.DateTimeField()

    def __str__(self):
        return f"{self.feedback_id} {self.user_id} {self.message}"

# Shopping_Cart Table
class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart_id} {self.user_id}"

# Cart_Items Table
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart_item_id} {self.cart_id} {self.book_id}"

# Subscriptions Table
class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

# Images Table
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    image_url = models.URLField()
