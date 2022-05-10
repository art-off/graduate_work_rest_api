from apps.food_projects.models import MenuItem, MenuOption


def prepare_menu_options_field(context, request):
    """
    Filter menu options for current user
    """
    menu_options_selector = context['adminform'].form.fields['allowed_options']
    menu_options_selector.queryset = MenuOption.objects.filter(project__owner=request.user)


def prepare_menu_items_field(context, request):
    """
    Filter menu items for current user
    """
    menu_items_selector = context['adminform'].form.fields['menu_items']
    menu_items_selector.queryset = MenuItem.objects.filter(project__owner=request.user)


def prepare_project_field(context, request, obj=None):
    """
    Filter project for current user and select first as default
    """
    project_selector = context['adminform'].form.fields.get('project')
    if not project_selector:
        return

    user_projects_queryset = request.user.foodproject_set

    # filter project by current user
    project_selector.queryset = user_projects_queryset
    if not obj:
        # select first project as default
        project_selector.initial = user_projects_queryset.first()
