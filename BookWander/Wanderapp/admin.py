from django.contrib import admin

from . import models 
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.UserPreferences)
admin.site.register(models.Review)
admin.site.register(models.Feedback)
admin.site.register(models.ShoppingCart)
admin.site.register(models.CartItem)
admin.site.register(models.Subscription)
admin.site.register(models.Image)