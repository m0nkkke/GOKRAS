from django.urls import path

from .views import MainPageView, RoutesListView

from .views import RoutePageView

urlpatterns = [
    path("", MainPageView.as_view(), name="route_main"), 
    path("routes/", RoutesListView.as_view(), name="routes_list"), 
    path('routes/<slug:slug>/', RoutePageView.as_view(), name='route_info'),
]

