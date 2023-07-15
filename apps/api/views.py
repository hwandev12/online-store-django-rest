from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer, SellerUserSerializer
from apps.product.models import Product, ProductImage
from rest_framework import mixins
from rest_framework import generics

from apps.authentication.models import SellerAccountModel, User
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
# ----------------- Seller User Api ----------------- #
    
# ----------------- Seller User Detail Api ----------------- #
class SellerUserDetailApiView(generics.RetrieveAPIView):
    queryset = SellerAccountModel.objects.all()
    serializer_class = SellerUserSerializer
# ----------------- Seller User Detail Api ----------------- #
    
product_lists = ProductListApiView.as_view()
product_detail = ProductDetailApiView.as_view()
seller_user_lists = SellerUserApiView.as_view()
seller_user_detail = SellerUserDetailApiView.as_view()