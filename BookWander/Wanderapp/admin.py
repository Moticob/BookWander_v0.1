from django.contrib import admin

from . import models 
# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre_name','slug', 'author', 'publication_date',
                    'price', 'in_stock'
                    ]
    list_filter = ['in_stock', 'genre_name', 'author']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'slug']
    prepopulated_fields = {'slug': ('genre_name',)}

admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.UserPreferences)
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_id','review_date' ,'book_id', 'rating', 'comment' ]

admin.site.register(models.Feedback)
admin.site.register(models.ShoppingCart)
admin.site.register(models.CartItem)
admin.site.register(models.Subscription)
admin.site.register(models.Image)