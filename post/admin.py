from django.contrib import admin
from .models import Post, Comment, Feed

class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'caption', 'images', 'created_at')
    fieldsets = (
        (None, {'fields': ('profile', 'caption', 'images', 'post_likes')}),
    )
    search_fields = ('profile',)
    # ordering = ('first_name',)
    filter_horizontal = ()

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','profile', 'post')


# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('post',)


#     def profile_display(self, obj):
#         return ", ".join([prof.profile for prof in Like.profile])
#     profile_display.short_description = "Profile"

admin.site.register(Post, PostAdmin)
# admin.site.register(Like, LikeAdmin)
# admin.site.register(Unlike)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feed)

