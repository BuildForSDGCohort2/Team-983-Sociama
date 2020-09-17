from django.contrib import admin
from .models import Profile, Follow, FriendReqest

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')
    # list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('user', 'first_name', 'last_name')}),
        ('Others', {'fields': ('friends', 'about', 'picture', 'cover')}),
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

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
admin.site.register(FriendReqest)

