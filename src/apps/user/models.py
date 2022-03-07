from django.contrib.auth.models import AbstractUser
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)

    project = models.ForeignKey("food_projects.FoodProject", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        pass
