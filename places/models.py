from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

class SluggedModel(models.Model):
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug and hasattr(self, 'name'):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Таблица категорий
class Category(SluggedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



""" Тут короч подкатегории если че добавить что-то можно"""

# Таблица тип заведения
class TypeEstablishment(SluggedModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='establishments')
    # places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return f"{self.name}"

# Таблица кухни
class TypesCuisine(SluggedModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cuisine')
    # places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return f"{self.name}"

class VisitingTime(SluggedModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='visittime')
    # places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return f"{self.name}"

"""------------------------------------------------------"""



class Place(SluggedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=300, blank=True, null=True, help_text="Макс.символов = 300")
    excerpt = models.TextField(max_length=150, blank=True, null=True, help_text="Макс.символов = 150")
    address = models.TextField(blank=True, null=True, help_text="Формат: 'ул.Сибирская, д. 92'")
    phone = models.TextField(blank=True, null=True, help_text="Формат: '+7 391 256-86-49'")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='places')
    latitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)  # Широта
    longitude = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True) # Долгота
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    people_quantity = models.IntegerField(blank=True, null=True)
    is_child_friendly = models.BooleanField(default=True, help_text="Доступно ли место для несовершеннолетних")
    avgprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Средняя цена посещения")
    additional_info = models.JSONField(blank=True, null=True, help_text="Дополнительная информация в формате JSON")

    establishment = models.ManyToManyField(TypeEstablishment, blank=True)
    cuisine = models.ManyToManyField(TypesCuisine, blank=True)
    visitingTime = models.ManyToManyField(VisitingTime, blank=True)

    visit_time = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        help_text="Введите время посещения в формате '00:00-00:00'"
    )

    def __str__(self):
        return self.name

# Таблица фотографий
class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(blank=True, default="default.jpg", upload_to="images")

    def __str__(self):
        return f"Photo for {self.place.name}"






