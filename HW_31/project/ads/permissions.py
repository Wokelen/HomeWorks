from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author
        else:
            raise Exception("Permission mistake")

        if request.user == owner:
            return True


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in [UserRole.ADMIN, UserRole.MODERATOR]:
            return True
