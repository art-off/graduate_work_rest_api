from django.db import models
from helpers.models import UUIDModel
from apps.user.models import User


class FoodProject(UUIDModel):
    name = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, editable=False)
