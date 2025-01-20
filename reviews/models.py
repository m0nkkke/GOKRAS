from django.db import models
from django.contrib.auth.models import User
from places.models import Place
from routes.models import Route
from django.conf import settings
from django.utils import timezone

# Create your models here.
# Таблица оценок
class ReviewPlaces(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='ratings')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True, related_name='ratings')
    rating = models.IntegerField(null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Rating by {self.user.username} for {'place' if self.place else 'route'}"
    
    class Meta:
        ordering = ['-created_at']