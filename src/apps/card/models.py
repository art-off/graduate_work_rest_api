from django.utils.translation import gettext_lazy as _
from django.db import models
from helpers.models import UUIDModel

from apps.food_projects.models import MenuItem, PromotionItem, FoodProject, MenuOption


class Order(UUIDModel):
    class Status(models.TextChoices):
        WAITING = 'WAITING', _('Waiting')
        EXECUTION = 'EXECUTION', _('Execution')
        DONE = 'DONE', _('Done')

    preferred_delivery_time = models.TimeField()
    customer_phone = models.CharField(max_length=30)
    status = models.CharField(max_length=120, choices=Status.choices, default=Status.WAITING)

    created_at = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)


class OrderMenuItem(UUIDModel):
    menu_item = models.ForeignKey(MenuItem, null=True, on_delete=models.SET_NULL)
    selected_options = models.ManyToManyField(MenuOption, blank=True)
    count = models.IntegerField()

    order = models.ForeignKey(Order, related_name='ordered_menu_items', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.menu_item} ({self.count})'


class OrderPromotions(UUIDModel):
    promotion = models.ForeignKey(PromotionItem, null=True, on_delete=models.SET_NULL)
    selected_options = models.ManyToManyField(MenuOption, blank=True)
    count = models.IntegerField()

    order = models.ForeignKey(Order, related_name='ordered_promotions', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.promotion} ({self.count})'
