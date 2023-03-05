from django.contrib import admin
from .models import Post, Category, Comment
from django.contrib.admin import TabularInline

class CommentInline(TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

    list_display = ('title', 'author', 'created_on', 'Category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)


# Register your models here.
