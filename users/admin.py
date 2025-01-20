from django.contrib import admin
from .models import Preference, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'preference_type', 'preference_value')
    search_fields = ('user__username', 'preference_type', 'preference_value')
    list_filter = ('preference_type',)

class CustomUserAdmin(UserAdmin):
    # Указываем, что будет отображаться в списке пользователей
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser', 'gender', 'phone']

    # Указываем, какие поля будут отображаться на страницах фильтрации
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    # Указываем, какие поля будут отображаться при редактировании
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Определяем, что будет отображаться в горизонтальном фильтре (если нужно)
    filter_horizontal = []

    # Указываем, что должно быть в форме для создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'gender', 'phone'),
        }),
    )

# Регистрация кастомного администратора для вашей модели User
admin.site.register(User, CustomUserAdmin)