from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404
from .models import Route

# Create your views here.
class MainPageView(ListView):
    model = Route
    template_name = 'routes_main.html'
    context_object_name = 'routes'

class RoutesListView(ListView):
    model = Route
    template_name = 'routes_list.html'
    context_object_name = 'routes'

class RoutePageView(DetailView):
    model = Route
    template_name = 'route_page.html'
    context_object_name = 'route'

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        return get_object_or_404(Route, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем все точки маршрута для текущего маршрута с загруженными местами
        context['route_points'] = self.object.route_points.select_related('place').all().order_by('order')
        return context