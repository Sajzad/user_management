from rest_framework.permissions import BasePermission
from users.models import User


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'manager'


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'customer'