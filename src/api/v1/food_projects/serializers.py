from rest_framework import serializers
from apps.food_projects.models import FoodProject, MenuItem, PromotionItem, MenuOption


class FoodProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodProject
        fields = '__all__'


class MenuOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOption
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    allowed_options = MenuOptionSerializer(many=True)
    type = serializers.CharField(source='type.name')

    class Meta:
        model = MenuItem
        fields = '__all__'


class PromotionItemSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    allowed_options = MenuOptionSerializer(many=True)

    class Meta:
        model = PromotionItem
        fields = '__all__'
