from django.contrib import admin
from .models import Post, Comment, Feed

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'caption', 'images', 'created_at')
    fieldsets = (
        (None, {'fields': ('profile', 'caption', 'images', 'post_likes')}),
    )
    search_fields = ('profile',)
    # ordering = ('first_name',)
    filter_horizontal = ()
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','profile', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feed)

