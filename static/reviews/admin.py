from django.contrib import admin
from .models import ReviewPlaces

# Register your models here.

@admin.register(ReviewPlaces)
class ReviewPlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_username', 'place', 'rating', 'comment')
    search_fields = ('user__username', 'place__name', 'route__route_name')
    list_filter = ('rating',)

    def get_user_username(self, obj):
        return obj.user.username if obj.user else 'Unknown user'
    get_user_username.short_description = 'Username'