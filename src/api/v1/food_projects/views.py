from .serializers import FoodProjectsSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class FoodProjectsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodProjectsSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.project)
        return Response(serializer.data)
