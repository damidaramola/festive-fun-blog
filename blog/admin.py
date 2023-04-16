from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# allows you to manage functionality of blog in admin view


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'blog']
    summernote_fields = ('body')
    list_filter = ('status', 'created_on')

#    allows you to manage comments made by Users


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'user_name', 'accepted', 'created_on')
    list_filter = ('accepted', 'created_on')
    search_fields = ('user_name', 'email', 'body')
  
    # accept comments from users on blog
    actions = ['accepted_comments']
   
    def accept_comments(self, request, queryset):
        queryset.update(accepted=True)