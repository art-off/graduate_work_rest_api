class QuerySetByCurrentUserProjectsMixin:
    """
    Use with `admin.ModelAdmin` classes where you want filter queryset by current user projects
    """
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(project__owner=request.user)