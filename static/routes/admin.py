from django.contrib import admin
from .models import Route, RoutePoint, FavoriteRoute, RouteChangeHistory

# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_name', 'people_count', 'budget', 'has_minors')
    search_fields = ('route_name',)
    list_filter = ('relation_type',)

@admin.register(RoutePoint)
class RoutePointAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'place', 'order')
    list_filter = ('route',)

@admin.register(FavoriteRoute)
class FavoriteRouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'route', 'added_at')

@admin.register(RouteChangeHistory)
class RouteChangeHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'user', 'change_date')