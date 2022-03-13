from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from utils import admin_form_helpers

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    non_superuser_fieldsets = (
        (None, {'fields': ('username', 'password', 'project',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'project',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        return super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if not request.user.is_superuser:
            return self.non_superuser_fieldsets
        return super().get_fieldsets(request, obj)

    def render_change_form(self, request, context, *args, obj=None, **kwargs):
        admin_form_helpers.prepare_project_field(context, request, obj)
        return super().render_change_form(request, context, *args, obj=obj, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(project__owner=request.user)
