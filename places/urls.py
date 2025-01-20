from django.urls import path
from .views import RestaurantsListView, ParksListView, RestsListView, PlaceDetailView

urlpatterns = [
    path("restaurants/", RestaurantsListView.as_view(), name="restaurants_list"),
    path("parks/", ParksListView.as_view(), name="parks_list"),
    path("rests/", RestsListView.as_view(), name="rests_list"),
    path('places/<slug:slug>/', PlaceDetailView.as_view(), name='place_info'),
]