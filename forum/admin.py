from django.contrib import admin
from .models import Comment, Post, Like, Dislike

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
