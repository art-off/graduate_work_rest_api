from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import FoodProjectsSerializer, MenuItemSerializer, PromotionItemSerializer
from apps.food_projects.models import MenuItem, PromotionItem


class AllQuerysetForSuperuserAndByProjectForOtherMixin:
    """
    Return all objects in queryset if user is superuser and only by project to others.
    Use with any ViewSet (where you use get_queryset)
    """
    queryset_object_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset_object_class.objects.all()
        return self.queryset_object_class.objects.filter(project=self.request.project)


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
