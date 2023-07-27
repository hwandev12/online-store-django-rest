from rest_framework import permissions
from rest_framework.response import Response

class DocumentIsOwnerPermission(permissions.BasePermission):
    message = "Sorry you are not owner of this order"        
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_buyer:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if obj.user == request.user.buyeraccountmodel:
            return True
        return False
    
class ProfileIsOwnerGeneralPermission(permissions.BasePermission):
    message = "Sorry redirect home page"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
        return False
    
class CustomModelPermissionToCheckWrite(permissions.BasePermission):
    message = "Actually this message doesn't show itself, but just in case"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_buyer:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if obj.user == request.user.buyeraccountmodel:
            return True
        return False
    
class SellerProductCreatePermission(permissions.BasePermission):
    message = "You don't have permission to create and edit in this page, Actually here we should show 404 page to redirect user to"
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_seller:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user.selleraccountmodel