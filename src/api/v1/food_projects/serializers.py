from rest_framework import serializers
from apps.food_projects.models import FoodProject, MenuItem, PromotionItem


class FoodProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodProject
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class PromotionItemSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = PromotionItem
        fields = '__all__'
