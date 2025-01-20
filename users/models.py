from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.conf import settings
from places.views import Place
from .managers import CustomUserManager

# Таблица предпочтений
class Preference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='preferences')
    preference_type = models.CharField(max_length=255)
    preference_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username}: {self.preference_type} - {self.preference_value}"
    
class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('W', 'Женский'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(blank=True, default="default.jpg", upload_to="images")
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    
    # Стандартные поля
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']  # username нужно в списке обязательных полей

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # Автоматическое заполнение username на основе email
        if not self.username and self.email:
            self.username = self.email
        super().save(*args, **kwargs)

        
class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        # Ограничиваем, чтобы пользователь не мог добавить одно место в избранное несколько раз
        unique_together = ('user', 'place')

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"
    
