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
    OrderSerializer
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
from rest_framework import mixins
from rest_framework import generics, viewsets
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
class BuyerUserApiView(viewsets.ReadOnlyModelViewSet):
    queryset = BuyerAccountModel.objects.all()
    serializer_class = BuyerUserSerializer
    
    permission_classes = [permissions.IsAdminUser]
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
class OrderApiView(viewsets.ReadOnlyModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = OrderSerializer
# ----------------- Order Api ----------------- #