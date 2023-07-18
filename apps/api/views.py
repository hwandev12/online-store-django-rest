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
    ProductImageSerializer
)
from apps.product.models import Product, ProductImage
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from apps.authentication.models import (
    SellerAccountModel,
    User,
    BuyerAccountModel
)
from rest_framework import permissions
import json

@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-lists", request=request, format=format),
        "products": reverse("products-api", request=request, format=format),
        "seller users": reverse("seller-users-api", request=request, format=format),
        "buyer users": reverse("buyer-users-api", request=request, format=format),
    })

# ----------------- Product Api ----------------- #
class ProductListApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
# ----------------- Product Api ----------------- #

# ----------------- Product Detail Api ----------------- #    
class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# ----------------- Product Detail Api ----------------- #    

# ----------------- Product Image Api ----------------- #    
class ProductImageApiView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
# ----------------- Product Image Api ----------------- #    

# ----------------- Seller User Api ----------------- #
class SellerUserApiView(generics.ListAPIView):
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- Seller User Api ----------------- #
    
# ----------------- Seller User Detail Api ----------------- #
class SellerUserDetailApiView(generics.RetrieveAPIView):
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
    lookup_field = 'first_name'
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- Seller User Detail Api ----------------- #

# ----------------- Buyer User Api ----------------- #
class BuyerUserApiView(generics.ListAPIView):
    queryset = BuyerAccountModel.objects.all()
    serializer_class = BuyerUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- Buyer User Api ----------------- #

# ----------------- Buyer User Detail Api ----------------- #
class BuyerUserDetailApiView(generics.RetrieveAPIView):
    queryset = BuyerAccountModel.objects.all()
    serializer_class = BuyerUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- Buyer User Detail Api ----------------- #

# ----------------- User Api ----------------- #
class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- User Api ----------------- #
# ----------------- User Detail Api ----------------- #
class UserDetailApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
# ----------------- User Detail Api ----------------- #


product_lists = ProductListApiView.as_view()
product_detail = ProductDetailApiView.as_view()
product_image_detail = ProductImageApiView.as_view()
seller_user_lists = SellerUserApiView.as_view()
seller_user_detail = SellerUserDetailApiView.as_view()
buyer_user_lists = BuyerUserApiView.as_view()
buyer_user_detail = BuyerUserDetailApiView.as_view()
user_lists = UserApiView.as_view()
user_detail = UserDetailApiView.as_view()