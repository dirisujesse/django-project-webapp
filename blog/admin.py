from django.contrib import admin
from .models import Post, Comment


class CommentAdmin(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Head', {'fields': ['title', 'author']}),
        ('Post Content', {'fields': ['content']}),
        ('Post Content', {'fields': ['date_pub'], 'classes': ['collapse']})
    ]
    inlines = [CommentAdmin]
    list_display = ('title', 'author', 'date_pub')
    list_filter = ['date_pub']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)