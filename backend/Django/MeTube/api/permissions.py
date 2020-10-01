from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if obj.user == request.user else False