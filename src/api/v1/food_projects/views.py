from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import FoodProjectsSerializer, MenuItemSerializer, PromotionItemSerializer
from apps.food_projects.models import MenuItem, PromotionItem
from helpers.mixins import AllQuerysetForSuperuserAndByProjectForOtherMixin


class FoodProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodProjectsSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.project)
        return Response(serializer.data)


class MenuItemViewSet(
    AllQuerysetForSuperuserAndByProjectForOtherMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = MenuItemSerializer
    queryset_object_class = MenuItem


class PromotionItemViewSet(
    AllQuerysetForSuperuserAndByProjectForOtherMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = PromotionItemSerializer
    queryset_object_class = PromotionItem
