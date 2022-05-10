from rest_framework import serializers

from apps.card.models import Order, OrderMenuItem, OrderPromotions
from api.v1.food_projects.serializers import MenuItemSerializer, PromotionItemSerializer


class OrderMenuItemsSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()

    class Meta:
        model = OrderMenuItem
        fields = '__all__'


class OrderPromotionsSerializer(serializers.ModelSerializer):
    promotion = PromotionItemSerializer()

    class Meta:
        model = OrderPromotions
        fields = '__all__'


class CreateOrderMenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenuItem
        fields = ('menu_item', 'selected_options', 'count',)


class CreateOrderPromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPromotions
        fields = ('promotion', 'selected_options', 'count',)


class OrderSerializer(serializers.ModelSerializer):
    ordered_menu_items = OrderMenuItemsSerializer(many=True)
    ordered_promotions = OrderPromotionsSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    ordered_menu_items = CreateOrderMenuItemsSerializer(many=True)
    ordered_promotions = CreateOrderPromotionsSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        ordered_menu_items_data = validated_data.pop('ordered_menu_items')
        ordered_promotions_data = validated_data.pop('ordered_promotions')

        order = Order.objects.create(**validated_data)

        for ordered_menu_item_data in ordered_menu_items_data:
            selected_options = ordered_menu_item_data.pop('selected_options')
            order_menu_item = OrderMenuItem(order=order, **ordered_menu_item_data)
            order_menu_item.save()
            for i in selected_options:
                order_menu_item.selected_options.add(str(i.id))
        for ordered_promotion_data in ordered_promotions_data:
            selected_options = ordered_promotion_data.pop('selected_options')
            order_promotion = OrderPromotions(order=order, **ordered_promotion_data)
            order_promotion.save()
            for i in selected_options:
                order_promotion.selected_options.add(str(i.id))
        return order
