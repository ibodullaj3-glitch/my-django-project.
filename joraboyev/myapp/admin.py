from django.contrib import admin
from telegram import User

# Register your models here.
from .models import User, Blogs
admin.site.register(User)
admin.site.register(Blogs)