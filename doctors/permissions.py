from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    """
    Allows access only to authenticated users with role='doctor'
    and only to their own doctor-related objects.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and getattr(request.user, "role", None) == "doctor"
        )

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated or getattr(user, "role", None) != "doctor":
            return False

        if hasattr(obj, "user"):
            return obj.user == user

        if hasattr(obj, "doctor"):
            return obj.doctor.user == user

        return False
