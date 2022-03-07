from rest_framework import serializers
from apps.food_projects.models import FoodProject, MenuItem


class FoodProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodProject
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
