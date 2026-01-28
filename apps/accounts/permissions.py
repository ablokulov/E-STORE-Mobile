from rest_framework.permissions import BasePermission


class Is_Admin(BasePermission):
    message = "Siz Admin emassz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin_role
    
    
class Is_Staff(BasePermission):
    message = "Siz Staff emas sz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff_role
    
 

class Is_User(BasePermission):
    message = "Siz User emassz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_user_role
    
