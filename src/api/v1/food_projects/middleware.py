from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.status import HTTP_404_NOT_FOUND

from apps.food_projects.models import FoodProject


def project_middleware(get_response):
    def middleware(request):
        # if not api path (then it is Admin) - not inject project to response
        if not _is_api_request(request):
            return get_response(request)

        project_id = request.headers.get('Project-Id')
        if project_id is None:
            return JsonResponse({'detail': 'project_id does not exist'}, status=HTTP_404_NOT_FOUND)

        try:
            project = FoodProject.objects.get(pk=project_id)
        except (ObjectDoesNotExist, ValidationError):
            project = None
        if project is None:
            return JsonResponse({'detail': 'Project not found'}, status=HTTP_404_NOT_FOUND)

        request.project = project

        return get_response(request)

    return middleware


# HELPERS
def _is_api_request(request):
    return request.path.startswith('/api') and ('/docs/' not in request.path)
