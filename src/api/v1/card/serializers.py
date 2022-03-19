from rest_framework import serializers

from apps.card.models import Order
from api.v1.food_projects.serializers import MenuItemSerializer, PromotionItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    promotions = PromotionItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
