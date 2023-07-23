from django.contrib import admin
from .models import forum, Discussion, Post, Replie


admin.site.register(Post)
admin.site.register(Replie)
admin.site.register(forum)
admin.site.register(Discussion)
