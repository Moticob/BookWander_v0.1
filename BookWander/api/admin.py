from django.contrib import admin

from . import models 
admin.site.register(models.User)
admin.site.register(models.Book)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Review)
admin.site.register(models.ShoppingCart)
admin.site.register(models.CartItem)