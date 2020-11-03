from django.contrib import admin
from .models import Profile, Follow

class ProfileAdmin(admin.ModelAdmin):
    # follower = len(Profile.followers)
    list_display = ('username', 'first_name', 'last_name', 'user')
    # list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('user', 'username', 'first_name', 'last_name', 'gender', 'age')}),
        ('Basic Info', {'fields': ('Hobbies', 'work', 'education', 'relationship', 'phone')}),
        ('Others', {'fields': ('followers', 'followings', 'about', 'picture', 'cover', 'country')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'first_name', 'last_name', 'about', 'picture', 'cover', 'country'),
        }),
    )
    search_fields = ('first_name',)
    ordering = ('first_name',)
    filter_horizontal = ()

class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')
    list_filter = ('follower',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow, FollowAdmin)

admin.site.site_header = 'Sociama Administration'
admin.site.site_title = 'Welcome To Sociama Network'
admin.site.index_title = 'Welcome To Sociama Network'
