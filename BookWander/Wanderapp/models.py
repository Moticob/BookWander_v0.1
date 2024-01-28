from django.db import models

# Create your models here.


# Users Table
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password_hash = models.CharField(max_length=255)
    registration_date = models.DateTimeField()

# Books Table
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image_url = models.URLField()

# Orders Table
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Order_Items Table
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

# User_Preferences Table
class UserPreferences(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=255)
    preferred_authors = models.CharField(max_length=255)
    notification_settings = models.CharField(max_length=255)

# Reviews Table
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField()

# Feedback Table
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    feedback_date = models.DateTimeField()

# Shopping_Cart Table
class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

# Cart_Items Table
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

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
