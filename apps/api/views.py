from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import (
    ProductSerializer,
    SellerUserSerializer,
    BuyerUserSerializer
)
from apps.product.models import Product, ProductImage
from rest_framework import mixins
from rest_framework import generics

from apps.authentication.models import (
    SellerAccountModel,
    User,
    BuyerAccountModel
)
from rest_framework import permissions
import json

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
    
product_lists = ProductListApiView.as_view()
product_detail = ProductDetailApiView.as_view()
seller_user_lists = SellerUserApiView.as_view()
seller_user_detail = SellerUserDetailApiView.as_view()
buyer_user_lists = BuyerUserApiView.as_view()
buyer_user_detail = BuyerUserDetailApiView.as_view()