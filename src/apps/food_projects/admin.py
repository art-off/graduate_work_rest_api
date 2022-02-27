from django.contrib import admin
from .models import FoodProject


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
