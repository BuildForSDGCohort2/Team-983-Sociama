from django.contrib import admin
from .models import Post, Like, Unlike, Comment, Feed

class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'caption', 'images', 'created_at')
    fieldsets = (
        (None, {'fields': ('profile', 'caption', 'images')}),
    )
    search_fields = ('profile',)
    # ordering = ('first_name',)
    filter_horizontal = ()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','profile', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Unlike)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feed)

