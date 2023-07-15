from rest_framework import serializers
from apps.product.models import Product, ProductCategory, ProductImage

from django.contrib.auth import get_user_model
from apps.authentication.models import SellerAccountModel, BuyerAccountModel, User

User = get_user_model()

class ProductImageSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductImage.objects.all())
    
    class Meta:
        model = Product
        fields = "__all__"
        
class SellerUserSerializer(serializers.ModelSerializer):
    owner_product = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SellerAccountModel
        fields = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'organization', 'owner_product']
        
    # write a method to get user information
    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
        }
        
class BuyerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerAccountModel
        fields = "__all__"
    
    
    