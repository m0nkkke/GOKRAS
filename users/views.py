from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Favorites
from places.views import Place
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator

class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = UserLoginForm # Изменил форму для того чтобы стили вернуть
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.get_user()  # Получаем объект пользователя
        login(self.request, user)  # Авторизуем пользователя
        return super().form_valid(form)
    
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()

        backend = 'users.backends.EmailBackend'  # Укажите ваш кастомный бэкенд

        login(self.request, user, backend=backend)

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ProfilePageView(TemplateView):
    template_name = 'users/profile.html'
    model = Favorites

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_places = Favorites.objects.filter(user=self.request.user)
        context['favorite_places'] = favorite_places

        for favorite in favorite_places:
            favorite.place.card_photo_url = f"/media/images/{favorite.place.slug}_card.jpg"

        context['photo_form'] = UserProfileForm(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            context = self.get_context_data()
            context['photo_form'] = form
            return self.render_to_response(context)

def user_logout(request):
    logout(request)
    return redirect('login') 

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, place_id):
        place = get_object_or_404(Place, id=place_id)  # Получаем место по ID
        user = request.user  # Получаем текущего авторизованного пользователя

        # Проверяем, не добавлено ли уже это место в избранное
        if Favorites.objects.filter(user=user, place=place).exists():
            return HttpResponseForbidden("Это место уже в вашем избранном!")

        # Добавляем место в избранное
        Favorites.objects.create(user=user, place=place)
        return redirect('profile')