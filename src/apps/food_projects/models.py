from django.db import models
from helpers.models import UUIDModel
from apps.user.models import User
from colorfield.fields import ColorField


class FoodProject(UUIDModel):
    # base fields
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo_image = models.ImageField()

    # address
    address = models.CharField(max_length=240)
    link_to_2gis = models.URLField()

    # style fields
    primary_app_color = ColorField(default='#FF0000')

    # app build fields
    appstore_api_key = models.CharField(max_length=120)
    playmarket_api_key = models.CharField(max_length=120)
    app_icon_asset = models.FileField(help_text='''
    Загрузите иконки, сгенерированные с помощью https://google.com. Также необходимо сжать в формат .zip.
    ''')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, editable=False)

    def __str__(self):
        return self.name


class MenuOption(UUIDModel):
    name = models.CharField(max_length=60)
    price = models.FloatField()

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price}'


class MenuItemType(UUIDModel):
    name = models.CharField(max_length=30)

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItem(UUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()

    allowed_options = models.ManyToManyField(MenuOption, blank=True)

    type = models.ForeignKey(MenuItemType, on_delete=models.SET_NULL, null=True, default=None)
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
