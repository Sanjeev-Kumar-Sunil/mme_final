from django.contrib import admin
from .models import Post,CommentAndLikes
# Register your models here.
admin.site.register(Post)
admin.site.register(CommentAndLikes)