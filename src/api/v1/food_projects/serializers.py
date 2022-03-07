from rest_framework import serializers
from apps.food_projects.models import FoodProject


class FoodProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodProject
        fields = '__all__'
