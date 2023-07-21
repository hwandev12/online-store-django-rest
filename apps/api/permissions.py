from rest_framework import permissions

class DocumentIsOwnerPermission(permissions.BasePermission):
    message = "Sorry you are not owner of this order"        
    
    def has_object_permission(self, request, view, obj):
    
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user.buyeraccountmodel
    
class ProfileIsOwnerPermission(permissions.BasePermission):
    message = "Sorry redirect home page"
    
    def has_object_permission(self, request, view, obj):
    
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user