from django.contrib import admin

from utils.admin_form_helpers import prepare_project_field
from helpers.mixins import QuerySetByCurrentUserProjectsMixin
from .models import Order


@admin.register(Order)
class AdminOrder(QuerySetByCurrentUserProjectsMixin, admin.ModelAdmin):
    list_display = ('customer_phone', 'preferred_delivery_time',
                    'selected_menu_items', 'selected_promotions',
                    'status',)

    filter_horizontal = ('menu_items', 'promotions',)

    @staticmethod
    def selected_menu_items(obj):
        return ", ".join([i.name for i in obj.menu_items.all()])

    @staticmethod
    def selected_promotions(obj):
        return ", ".join([i.name for i in obj.promotions.all()])

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        prepare_project_field(context, request, obj)
        return super().render_change_form(request, context, add, change, form_url, obj)
