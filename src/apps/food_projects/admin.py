from django.contrib import admin
from .models import FoodProject, MenuItem, PromotionItem


class QuerySetByCurrentUserProjectsMixin:
    """
    Use with `admin.ModelAdmin` classes where you want filter queryset by current user projects
    """
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(project__owner=request.user)


@admin.register(FoodProject)
class AdminFoodProject(admin.ModelAdmin):
    list_display = ('name', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset
        return queryset.filter(owner=request.user)


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin, QuerySetByCurrentUserProjectsMixin):
    list_display = ('name', 'description', 'price')

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        _prepare_projects_field(context, request)
        return super().render_change_form(request, context, add, change, form_url, obj)


@admin.register(PromotionItem)
class AdminPromotionItem(admin.ModelAdmin, QuerySetByCurrentUserProjectsMixin):
    list_display = ('name', 'selected_menu_items', 'price')

    def selected_menu_items(self, obj):
        return ", ".join([i.name for i in obj.menu_items.all()])

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        _prepare_projects_field(context, request)
        _prepare_menu_items_field(context, request)
        return super().render_change_form(request, context, add, change, form_url, obj)


# HELPERS
def _prepare_menu_items_field(context, request):
    """
    Filter menu items for current user
    """
    menu_items_selector = context['adminform'].form.fields['menu_items']
    menu_items_selector.queryset = MenuItem.objects.filter(project__owner=request.user)


def _prepare_projects_field(context, request):
    """
    Filter project for current user and select first as default
    """
    project_selector = context['adminform'].form.fields['project']

    user_projects_queryset = request.user.foodproject_set
    # select first project as default
    project_selector.initial = user_projects_queryset.first()
    # filter project by current user
    project_selector.queryset = user_projects_queryset
