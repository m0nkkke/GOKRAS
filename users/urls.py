from django.urls import path
from .views import UserLoginView, UserRegisterView, ProfilePageView, user_logout, AddToFavoritesView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name='login'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("profile/", ProfilePageView.as_view(), name='profile'),
    path('add-to-favorites/<int:place_id>/', AddToFavoritesView.as_view(), name='add_to_favorites'),
    path("logout/", user_logout, name='logout'),
]