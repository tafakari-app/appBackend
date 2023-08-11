from django.contrib import admin
from .models import Post, PostComment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ( 'author', 'emotions', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


admin.site.register(Post,PostAdmin)

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'parent', 'created_at', 'updated_at')
    list_filter = ('author', 'parent', 'created_at', 'updated_at')
    search_fields = ('comment', 'author', 'parent', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)




admin.site.register(PostComment,PostCommentAdmin)
