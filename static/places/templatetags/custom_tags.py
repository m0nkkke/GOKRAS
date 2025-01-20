from django import template
import os
from django.conf import settings

register = template.Library()
@register.inclusion_tag('../templates/places/components/place_card.html')
def place_card(place):
    """
    Отображает карточку места.

    :param post: Объект карточки для отображения.
    :return: Контекст для шаблона карточки места.
    """
    return {
        'place': place,
    }

@register.inclusion_tag('../templates/places/components/filters_sidebar.html')
def filters_sidebar(filters):
    """
    Отображает панель фильтрации.

    :param filters: Словарь с фильтрами, передаваемый из представления.
    :return: Контекст для шаблона фильтра места.
    """
    return filters

@register.filter
def file_exists(file_path):
    """
    Проверяет наличие файла в MEDIA_ROOT.
    """
    if not file_path.startswith('/media/'):
        return False  # Если путь некорректный.
    
    # Удаляем /media/ из пути и формируем полный путь
    relative_path = file_path.replace('/media/', '')
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
    
    # Логируем путь для отладки (можно временно включить)
    print(f"Checking file: {full_path}")
    
    return os.path.exists(full_path)