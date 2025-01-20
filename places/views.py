from django.shortcuts import redirect
from .models import Place, Category, TypeEstablishment, TypesCuisine, VisitingTime
from django.views.generic import ListView, DetailView
from .models import Place
from math import floor
from django.shortcuts import get_object_or_404
from reviews.models import ReviewPlaces
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



class FilterQuerysetMixin:
    def apply_filters(self, queryset):
        filters = self.request.GET

        # Фильтры по типу
        if 'type' in filters:
            types = filters.getlist('type')
            queryset = queryset.filter(establishment__slug__in=types)

        # Фильтры по кухне
        if 'cuisine' in filters:
            cuisines = filters.getlist('cuisine')
            queryset = queryset.filter(cuisine__slug__in=cuisines)

        # Фильтры по времени
        if 'time' in filters:
            times = filters.getlist('time')
            queryset = queryset.filter(visitingTime__slug__in=times)

        # Фильтры по бюджету
        budget_min = filters.get('budget_min')
        budget_max = filters.get('budget_max')
        if budget_min:
            queryset = queryset.filter(avgprice__gte=budget_min)
        if budget_max:
            queryset = queryset.filter(avgprice__lte=budget_max)

        return queryset.distinct()

    def get_queryset(self):
        queryset = Place.objects.filter(category__slug=self.current_category_slug)
        return self.apply_filters(queryset)


class CommonContextMixin:
    current_category_slug = None  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем фотографии и рейтинг
        for place in context.get('place_list', []):
            image_name = f"/media/images/{place.slug}_card.jpg"
            place.card_photo_url = image_name
            place.rating = calculate_rating(place)

        # Получаем текущую категорию
        current_category = Category.objects.get(slug=self.current_category_slug)
        context['current_category'] = current_category

        # Добавляем категории и фильтры
        context['categories'] = Category.objects.all()
        context['type_establishments'] = TypeEstablishment.objects.filter(category__slug=self.current_category_slug)
        context['types_cuisine'] = TypesCuisine.objects.filter(category__slug=self.current_category_slug)
        context['visiting_times'] = VisitingTime.objects.filter(category__slug=self.current_category_slug)

        # Формируем словарь filters
        context['filters'] = {
            'categories': context['categories'],
            'type_establishments': context['type_establishments'],
            'types_cuisine': context['types_cuisine'],
            'visiting_times': context['visiting_times'],
            'current_category': context['current_category'],
        }

        # Передаем выбранные фильтры в контекст
        filters = self.request.GET
        context['selected_types'] = filters.getlist('type')
        context['selected_cuisines'] = filters.getlist('cuisine')
        context['selected_times'] = filters.getlist('time')
        context['budget_min'] = filters.get('budget_min', '')
        context['budget_max'] = filters.get('budget_max', '')

        return context

class RestaurantsListView(CommonContextMixin, FilterQuerysetMixin, ListView):
    model = Place
    template_name = 'restaurants_list.html' 
    context_object_name = 'place_list'
    current_category_slug = 'restoran'
    paginate_by = 6 

class ParksListView(CommonContextMixin, FilterQuerysetMixin, ListView):
    model = Place
    template_name = 'parks_list.html' 
    context_object_name = 'place_list'
    current_category_slug = 'park' 
    paginate_by = 6  

class RestsListView(CommonContextMixin, FilterQuerysetMixin, ListView):
    model = Place
    template_name = 'rests_list.html'  
    context_object_name = 'place_list'
    current_category_slug = 'dosug'  
    paginate_by = 6 

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place_info.html'
    context_object_name = 'place'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        return get_object_or_404(Place, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place = self.get_object()
        context['reviews'] = ReviewPlaces.objects.filter(place=place)
        return context

    def post(self, request, *args, **kwargs):
        place = self.get_object()
        
        # Получаем данные из формы
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        # Создаем новый отзыв, если комментарий и рейтинг присутствуют
        if comment and rating:
            ReviewPlaces.objects.create(
                user=request.user,  # Получаем текущего пользователя через request.user
                place=place,
                comment=comment,
                rating=int(rating)
            )
        
        # После добавления отзыва, перенаправляем на страницу этого места
        return redirect('place_info', slug=place.slug)
    

def calculate_rating(place):
        if place.rating is not None:
            full_stars = floor(place.rating)
            empty_stars = 5 - full_stars

            place.rating_stars = range(full_stars)
            place.empty_stars = range(empty_stars)
        else:
            place.rating_stars = []
            place.empty_stars = range(5)
        return place