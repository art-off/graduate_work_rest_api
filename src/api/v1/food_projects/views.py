from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import FoodProjectsSerializer, MenuItemSerializer
from apps.food_projects.models import MenuItem


class FoodProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodProjectsSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.project)
        return Response(serializer.data)


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return MenuItem.objects.all()
        return MenuItem.objects.filter(project=self.request.project)
