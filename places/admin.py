from django.contrib import admin
from .models import Category, Place, Photo, TypeEstablishment, TypesCuisine, VisitingTime

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Отображение ID, названия и родительской категории
    search_fields = ('name',)  # Поиск по названию категории
    
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'rating', 'is_child_friendly')
    search_fields = ('name', 'address')
    list_filter = ('category',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'photo')
    search_fields = ('place__name',)

@admin.register(TypeEstablishment)
class TypeEstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)

@admin.register(TypesCuisine)
class TypeEstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)

@admin.register(VisitingTime)
class TypeEstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name',)