from django.contrib import admin
from django.db.models import Q
from .models import FoodProject, MenuItem


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


def _get_only_current_user_menu_items(request, queryset):
    user_projects = FoodProject.objects.filter(owner=request.user)

    any_user_project_filter_condition = Q()
    for user_project in user_projects:
        any_user_project_filter_condition = any_user_project_filter_condition | Q(project=user_project)
    return queryset.filter(any_user_project_filter_condition)


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin):
    list_display = ('name', 'description')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return _get_only_current_user_menu_items(request, queryset)

        # user_projects = FoodProject.objects.filter(owner=request.user)
        #
        # any_user_project_filter_condition = Q()
        # for user_project in user_projects:
        #     any_user_project_filter_condition = any_user_project_filter_condition | Q(project=user_project)
        # return queryset.filter(any_user_project_filter_condition)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        project_selector = context['adminform'].form.fields['project']

        # select first project as default
        project_selector.initial = 1
        # filter project by current user
        project_selector.queryset = FoodProject.objects.filter(owner=request.user)

        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
