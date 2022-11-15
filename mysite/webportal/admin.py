from django.contrib import admin
from .models import User, Request, Category

admin.site.register(User)
admin.site.register(Request)
admin.site.register(Category)