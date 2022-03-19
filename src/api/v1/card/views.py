from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.card.models import Order
from .serializers import OrderSerializer, CreateOrderSerializer
from helpers.mixins import AllQuerysetForSuperuserAndByProjectForOtherMixin
from helpers.permission_classes import SecretKeyPermission


class OrderViewSet(
    AllQuerysetForSuperuserAndByProjectForOtherMixin,
    viewsets.ModelViewSet
):
    permission_classes = (SecretKeyPermission,)
    queryset_object_class = Order

    def create(self, request, *args, **kwargs):
        # Override because we need get 'project' field from headers
        data = request.data
        data['project'] = request.project.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        return OrderSerializer
