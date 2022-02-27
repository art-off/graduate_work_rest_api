from django.contrib import admin
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


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin):
    list_display = ('name', 'description')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset
        return queryset.filter(project__owner=request.user)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        project_selector = context['adminform'].form.fields['project']

        user_projects_queryset = request.user.foodproject_set
        # select first project as default
        project_selector.initial = user_projects_queryset.first()
        # filter project by current user
        project_selector.queryset = user_projects_queryset

        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
