from rest_framework import permissions
from django.conf import settings


class SecretKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        secret_key = request.headers.get('Secret-Key')
        return secret_key in settings.SECRET_AUTH_KEYS
