from django.db import models
from helpers.models import UUIDModel
from apps.user.models import User
from colorfield.fields import ColorField


class FoodProject(UUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo_image = models.ImageField()
    address = models.CharField(max_length=240)
    linkTo2Gis = models.URLField()
    primary_app_color = ColorField(default='#FF0000')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, editable=False)

    def __str__(self):
        return self.name


class MenuOption(UUIDModel):
    name = models.CharField(max_length=60)
    price = models.FloatField()

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'


class MenuItem(UUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()

    allowed_options = models.ManyToManyField(MenuOption, blank=True)

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}₽'


class PromotionItem(UUIDModel):
    class TextColor(models.TextChoices):
        WHITE = 'WHITE'
        BLACK = 'BLACK'

    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    over_image_text_color = models.CharField(max_length=20, choices=TextColor.choices)

    menu_items = models.ManyToManyField(MenuItem)
    allowed_options = models.ManyToManyField(MenuOption, blank=True)

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'
