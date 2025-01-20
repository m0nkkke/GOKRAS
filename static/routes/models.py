from django.db import models
from django.contrib.auth.models import User
from places.models import Place
from django.conf import settings
from slugify import slugify

# Create your models here.

class SluggedModel(models.Model):
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug and hasattr(self, 'name'):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Таблица маршрутов
class Route(SluggedModel):
    route_name = models.CharField(max_length=255)
    people_count = models.IntegerField()
    relation_type = models.CharField(max_length=255, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=1024, blank=True, null=True, default='def')
    excerpt = models.TextField(max_length=200, default='def', blank=True, null=True, help_text="Макс.символов = 150")
    total_time = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    has_minors = models.BooleanField(default=False, help_text="Есть ли несовершеннолетние в группе")

    def __str__(self):
        return self.route_name

# Таблица истории изменений маршрутов
class RouteChangeHistory(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='change_history')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='route_changes')
    change_description = models.TextField()
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change in {self.route.route_name} by {self.user.username}"
    
# Таблица избранных маршрутов
class FavoriteRoute(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='favorite_routes')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} favorited {self.route.route_name}"
    
# Таблица пунктов маршрута
class RoutePoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='route_points')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='in_routes')
    description = models.TextField(max_length=512, blank=True, null=True)
    total_time = models.IntegerField(default=0)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.place.name} in {self.route.route_name}"