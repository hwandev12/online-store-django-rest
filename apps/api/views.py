from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
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
    BuyerProfileSerializer,
    SellerProfileSerializer,
    # for registration
    SellerUserRegisterSerializer,
    BuyerUserRegisterSerializer
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
from dj_rest_auth.registration.views import RegisterView
from . import permissions as custom_perm

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound

from apps.authentication.models import (
    SellerAccountModel,
    User,
    BuyerAccountModel,
    BuyerProfile,
    SellerProfile
)
from rest_framework import permissions
import json

from .permissions import (
    DocumentIsOwnerPermission,
)

from django_filters import rest_framework as filters

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "products": reverse("api-product", request=request, format=format),
    })

# ----------------- Product Api ----------------- #
class ProductListApiView(mixins.ListModelMixin,
                         generics.GenericAPIView):
    """_Summary of This API_

    Description:
        content: Here is public where each user even sellers can see their products online

    Returns:
        _type_: _Read Only View_
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# ----------------- Product Api ----------------- #

# ----------------- Product Detail Api ----------------- #
class ProductDetailApiView(mixins.RetrieveModelMixin,
                           generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# ----------------- Product Detail Api ----------------- #

# ----------------- Product Create Api ----------------- #
class ProductCreateApiView(mixins.CreateModelMixin,
                           generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [custom_perm.SellerProductCreatePermission]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# ----------------- Product Create Api ----------------- #

# ----------------- Product Update Api ----------------- #
class ProductUpdateApiView(mixins.UpdateModelMixin,
                           mixins.RetrieveModelMixin,
                           generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [custom_perm.SellerProductCreatePermission]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
# ----------------- Product Update Api ----------------- #

# ----------------- Product Delete Api ----------------- #
class ProductDeleteApiView(mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = [custom_perm.SellerProductCreatePermission]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# ----------------- Product Delete Api ----------------- #

# ----------------- Seller User Api ----------------- #
class SellerUserApiView(viewsets.ModelViewSet):
    """_This page is only for admin and other permitted users to get seller users data for dashboard and other purposes_

    Right:
         _Just for admin rights_
    """
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = 'first_name'
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
# ----------------- Seller User Api ----------------- #

# ----------------- Seller Profile Api ----------------- #
from itertools import chain
class GeneralProfileApiView(mixins.RetrieveModelMixin,
                           generics.GenericAPIView):
    
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = "first_name"
    
    def get_queryset(self):
        try:
            if self.request.user.is_buyer:
                return BuyerAccountModel.objects.all()
            return SellerAccountModel.objects.all()
        except ValueError as e:
            return e
        
    def get_serializer_class(self):
        try:
            if self.request.user.is_buyer:
                return BuyerUserSerializer
            return SellerUserSerializer
        except ValueError as e:
            return e
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
    permission_classes = [permissions.IsAuthenticated, custom_perm.ProfileIsOwnerGeneralPermission]
    
# ----------------- Seller Profile Api ----------------- #

# ----------------- Seller Profile Update Api ----------------- #
class GeneralProfileUpdateApiView(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              generics.GenericAPIView):
    
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = 'first_name'
    permission_classes = [custom_perm.ProfileIsOwnerGeneralPermission]
    
    def get_queryset(self):
        try:
            if self.request.user.is_buyer:
                return BuyerAccountModel.objects.all()
            return SellerAccountModel.objects.all()
        except ValueError as e:
            return e
        
    def get_serializer_class(self):
        try:
            if self.request.user.is_buyer:
                return BuyerUserSerializer
            return SellerUserSerializer
        except ValueError as e:
            return e
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
# ----------------- Seller Profile Update Api ----------------- #

# ----------------- Seller Profile Delete Api ----------------- #
class GeneralProfileDeleteApiView(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    
    """
    That could be for deletion account. But then we can update to complex one
    """
    
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = "first_name"
    permission_classes = [custom_perm.ProfileIsOwnerGeneralPermission]
    
    def get_queryset(self):
        try:
            if self.request.user.is_buyer:
                return BuyerAccountModel.objects.all()
            return SellerAccountModel.objects.all()
        except ValueError as e:
            return e
        
    def get_serializer_class(self):
        try:
            if self.request.user.is_buyer:
                return BuyerUserSerializer
            return SellerUserSerializer
        except ValueError as e:
            return e
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
# ----------------- Seller Profile Delete Api ----------------- #

# ----------------- Buyer User Api ----------------- #
class BuyerUserApiView(viewsets.ModelViewSet):
    queryset = BuyerAccountModel.objects.all()
    serializer_class = BuyerUserSerializer
    lookup_field = "first_name"
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
# ----------------- Buyer User Api ----------------- #

# ----------------- User Api ----------------- #
class UserApiView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
# ----------------- User Api ----------------- #

# ----------------- Product Category Api ----------------- #
class ProductCategoryApiView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
# ----------------- Product Category Api ----------------- #

# ----------------- Comment Api ----------------- #
class CommentApiView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    permission_classes = [custom_perm.CustomModelPermissionToCheckWrite,]
# ----------------- Comment Api ----------------- #
# ----------------- Rating Api ----------------- #
class RatingProductApiView(viewsets.ReadOnlyModelViewSet):
    queryset = RatingProduct.objects.all()
    serializer_class = RatingProductSerializer
    
    permission_classes = [permissions.IsAuthenticated]
# ----------------- Rating Api ----------------- #
# ----------------- Cart Api ----------------- #
class CheckoutItemApiView(viewsets.ReadOnlyModelViewSet):
    queryset = CheckoutItem.objects.all()
    serializer_class = CheckoutItemProductSerializer
    
    permission_classes = [permissions.IsAuthenticated]
# ----------------- Cart Api ----------------- #
# ----------------- Order Api ----------------- #
class OrderApiView(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = OrderSerializer
    
    permission_classes = [permissions.IsAuthenticated]             
     
    
    def get_queryset(self):
        try:
            user = self.request.user.buyeraccountmodel
            return Checkout.objects.filter(user=user)
        except BuyerAccountModel.DoesNotExist:
            raise NotFound
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
# ----------------- Order Api ----------------- #

# ----------------- For User Registration ----------------- #
class SellerRegisterApiView(RegisterView):
    serializer_class = SellerUserRegisterSerializer
class BuyerRegisterApiView(RegisterView):
    serializer_class = BuyerUserRegisterSerializer
# ----------------- For User Registration ----------------- #

