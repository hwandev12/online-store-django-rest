from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import (
    ProductSerializer,
    SellerUserSerializer,
    BuyerUserSerializer,
    AllUserSerializer,
    ProductImageSerializer,
    ProductCategorySerializer,
    CommentSerializer,
    RatingProductSerializer,
    CheckoutItemProductSerializer,
    OrderSerializer,
    BuyerProfileSerializer
)
from apps.product.models import (
    Product,
    ProductImage,
    ProductCategory,
    Comment,
    RatingProduct,
    CheckoutItem,
    Checkout
)
from rest_framework import mixins, permissions, status
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from apps.authentication.models import (
    SellerAccountModel,
    User,
    BuyerAccountModel,
    BuyerProfile,
    SellerProfile
)
from rest_framework import permissions
import json

from .permissions import DocumentIsOwnerPermission, ProfileIsOwnerPermission

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-lists", request=request, format=format),
        "products": reverse("products-api", request=request, format=format),
        "seller users": reverse("seller-users-api", request=request, format=format),
        "buyer users": reverse("buyer-users-api", request=request, format=format),
    })

# ----------------- Product Api ----------------- #
class ProductListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    
# ----------------- Product Api ----------------- #

# ----------------- Product Image Api ----------------- #    
class ProductImageApiView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
# ----------------- Product Image Api ----------------- #    

# ----------------- Seller User Api ----------------- #
class SellerUserApiView(viewsets.ReadOnlyModelViewSet):
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = 'first_name'
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- Seller User Api ----------------- #

# ----------------- Buyer User Api ----------------- #
class BuyerUserApiView(viewsets.ModelViewSet):
    queryset = BuyerAccountModel.objects.all()
    serializer_class = BuyerUserSerializer
    lookup_field = "first_name"
    
    permission_classes = [ProfileIsOwnerPermission]
# ----------------- Buyer User Api ----------------- #

# ----------------- User Api ----------------- #
class UserApiView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- User Api ----------------- #

# ----------------- Product Category Api ----------------- #
class ProductCategoryApiView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
# ----------------- Product Category Api ----------------- #

# ----------------- Comment Api ----------------- #
class CommentApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# ----------------- Comment Api ----------------- #
# ----------------- Rating Api ----------------- #
class RatingProductApiView(viewsets.ReadOnlyModelViewSet):
    queryset = RatingProduct.objects.all()
    serializer_class = RatingProductSerializer
# ----------------- Rating Api ----------------- #
# ----------------- Cart Api ----------------- #
class CheckoutItemApiView(viewsets.ReadOnlyModelViewSet):
    queryset = CheckoutItem.objects.all()
    serializer_class = CheckoutItemProductSerializer
# ----------------- Cart Api ----------------- #
# ----------------- Order Api ----------------- #
class OrderApiView(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = OrderSerializer
    
    permission_classes = [DocumentIsOwnerPermission, ]        
    
    def get_queryset(self):
        if self.request.user.is_buyer:
            user = self.request.user.buyeraccountmodel
            return Checkout.objects.filter(user=user)
        else:
            # show error log here later
            pass
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
# ----------------- Order Api ----------------- #

# ----------------- BuyerProfile Api ----------------- #
class BuyerProfileApiView(viewsets.ModelViewSet):
    queryset = BuyerProfile.objects.all()
    serializer_class = BuyerProfileSerializer
    
    def get_queryset(self):
        if self.request.user.is_buyer:
            return BuyerProfile.objects.filter(user=self.request.user.buyeraccountmodel)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    permission_classes = [DocumentIsOwnerPermission]
# ----------------- BuyerProfile Api ----------------- #