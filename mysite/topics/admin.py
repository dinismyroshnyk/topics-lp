from django.contrib import admin
from .models import Topic, Comment, Profile

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Profile)