from rest_framework.permissions import BasePermission


class IsSupervisor(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "SUPERVISOR"
        )

class IsDriver(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "DRIVER"
        )

class IsRouter(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "ROUTER"
        )
    


class IsMaintenance(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.userprofile.role == "Maintenance"
        )
