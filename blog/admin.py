from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('user',)
    list_per_page = 50

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
