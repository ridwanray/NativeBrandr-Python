from django.contrib import admin

from .models import Category, Design,UserProfile
admin.site.register(Category)
admin.site.register(Design)
admin.site.register(UserProfile)