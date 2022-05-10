from django.contrib import admin

from helpers.mixins import QuerySetByCurrentUserProjectsMixin
from utils.admin_form_helpers import prepare_project_field, prepare_menu_items_field, prepare_menu_options_field
from .models import FoodProject, MenuItem, PromotionItem, MenuOption


@admin.register(FoodProject)
class AdminFoodProject(admin.ModelAdmin):
    list_display = ('name', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset
        return queryset.filter(owner=request.user)


@admin.register(MenuOption)
class AdminMenuOption(QuerySetByCurrentUserProjectsMixin, admin.ModelAdmin):
    list_display = ('name', 'price',)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        prepare_project_field(context, request, obj)
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(MenuItem)
class AdminMenuItem(QuerySetByCurrentUserProjectsMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)

    filter_horizontal = ('allowed_options',)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        prepare_project_field(context, request, obj)
        prepare_menu_options_field(context, request)
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(PromotionItem)
class AdminPromotionItem(QuerySetByCurrentUserProjectsMixin, admin.ModelAdmin):
    list_display = ('name', 'selected_menu_items', 'price',)

    filter_horizontal = ('menu_items', 'allowed_options',)

    @staticmethod
    def selected_menu_items(obj):
        return ", ".join([i.name for i in obj.menu_items.all()])

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        prepare_project_field(context, request, obj)
        prepare_menu_items_field(context, request)
        prepare_menu_options_field(context, request)
        return super().render_change_form(request, context, add, change, form_url, obj)
