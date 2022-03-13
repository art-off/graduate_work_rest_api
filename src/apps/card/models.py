from django.utils.translation import gettext_lazy as _
from django.db import models
from helpers.models import UUIDModel

from apps.food_projects.models import MenuItem, PromotionItem, FoodProject


class Order(UUIDModel):
    class Status(models.TextChoices):
        WAITING = 'WAITING', _('Waiting')
        EXECUTION = 'EXECUTION', _('Execution')
        DONE = 'DONE', _('Done')

    menu_items = models.ManyToManyField(MenuItem, blank=True)
    promotions = models.ManyToManyField(PromotionItem, blank=True)

    preferred_delivery_time = models.TimeField()
    customer_phone = models.CharField(max_length=30)
    status = models.CharField(max_length=120, choices=Status.choices, default=Status.WAITING)

    project = models.ForeignKey(FoodProject, on_delete=models.CASCADE)
