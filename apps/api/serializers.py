from rest_framework import serializers
from apps.product.models import Product, ProductCategory, ProductImage

from django.contrib.auth import get_user_model
from apps.authentication.models import SellerAccountModel, BuyerAccountModel, User

class ProductImageSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductImage.objects.all())
    
    class Meta:
        model = Product
        fields = "__all__"
        
class SellerUserSerializer(serializers.HyperlinkedModelSerializer):
    owner_product = serializers.HyperlinkedRelatedField(many=True, view_name="product-detail-api", queryset=Product.objects.all())
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SellerAccountModel
        fields = ['id', 'user', 'first_name', 'last_name', 'phone_number', 'organization', 'owner_product']
        
    # write a method to get user information
    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "is_staff": obj.user.is_staff,
            "is_superuser": obj.user.is_superuser,
            "is_active": obj.user.is_active
        }
        
class BuyerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerAccountModel
        fields = "__all__"
    

class AllUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
    
    