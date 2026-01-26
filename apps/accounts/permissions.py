from rest_framework.permissions import BasePermission


class Is_Admin(BasePermission):
    message = "Siz admin emassz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
    
    
class Is_Staff(BasePermission):
    message = "Siz Admin va Operator ham emassz"
    
    def has_permission(self, request, view):
        return (
        request.user.is_authenticated
        and request.user.role in ["ADMIN", "STAFF"]
        )
    
    
class Is_User(BasePermission):
    message = "Siz user emassz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_user
