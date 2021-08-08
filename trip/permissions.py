from rest_framework.permissions import BasePermission
from rest_framework import permissions

class TripIsOwnerOrReadOnly(BasePermission): 
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.guide