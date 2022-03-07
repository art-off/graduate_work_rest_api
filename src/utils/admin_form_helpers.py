from apps.food_projects.models import MenuItem


def prepare_menu_items_field(context, request):
    """
    Filter menu items for current user
    """
    menu_items_selector = context['adminform'].form.fields['menu_items']
    menu_items_selector.queryset = MenuItem.objects.filter(project__owner=request.user)


def prepare_project_field(context, request):
    """
    Filter project for current user and select first as default
    """
    project_selector = context['adminform'].form.fields.get('project')
    if not project_selector:
        return

    user_projects_queryset = request.user.foodproject_set
    print(user_projects_queryset)
    # select first project as default
    # TODO: maybe it will breake if selected second (of later) project
    # project_selector.initial = user_projects_queryset.first()
    # filter project by current user
    project_selector.queryset = user_projects_queryset
