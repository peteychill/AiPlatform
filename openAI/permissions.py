from rest_framework.permissions import BasePermission
from django.conf import settings

class IsAllowedClient(BasePermission):

    def has_permission(self, request, view):
        allowed = getattr(settings, 'ALLOWED_CLIENT_IDS')
        token = request.auth
        app = getattr(token, 'application', None)
        return app and app.client_id in allowed