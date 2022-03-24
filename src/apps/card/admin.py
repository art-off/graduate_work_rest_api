from django.contrib import admin

from utils.admin_form_helpers import prepare_project_field
from helpers.mixins import QuerySetByCurrentUserProjectsMixin
from .models import Order, OrderMenuItem, OrderPromotions

from apps.food_projects.models import PromotionItem, MenuItem


class FilteredFormFiledMixin:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if request.user.is_superuser:
            return formfield
        if formfield.queryset.model in (PromotionItem, MenuItem):
            formfield.queryset = formfield.queryset.filter(project__owner=request.user)
        return formfield


class MenuItemInline(FilteredFormFiledMixin, admin.TabularInline):
    model = OrderMenuItem
    fk_name = 'order'
    extra = 0


class PromotionInline(FilteredFormFiledMixin, admin.TabularInline):
    model = OrderPromotions
    fk_name = 'order'
    extra = 0


@admin.register(Order)
class AdminOrder(QuerySetByCurrentUserProjectsMixin, admin.ModelAdmin):
    list_display = ('customer_phone', 'preferred_delivery_time', 'status',)

    inlines = (MenuItemInline, PromotionInline,)

    @staticmethod
    def selected_menu_items(obj):
        return ", ".join([i.name for i in obj.menu_items.all()])

    @staticmethod
    def selected_promotions(obj):
        return ", ".join([i.name for i in obj.promotions.all()])

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        prepare_project_field(context, request, obj)
        return super().render_change_form(request, context, add, change, form_url, obj)
