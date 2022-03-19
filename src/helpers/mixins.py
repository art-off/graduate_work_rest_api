class QuerySetByCurrentUserProjectsMixin:
    """
    Use with `admin.ModelAdmin` classes where you want filter queryset by current user projects
    """
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(project__owner=request.user)


class AllQuerysetForSuperuserAndByProjectForOtherMixin:
    """
    Return all objects in queryset if user is superuser and only by project to others.
    Use with any ViewSet (where you use get_queryset)
    """
    queryset_object_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset_object_class.objects.all()
        return self.queryset_object_class.objects.filter(project=self.request.project)
