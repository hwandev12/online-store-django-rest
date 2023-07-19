from rest_framework import serializers
from apps.product.models import (
    Product,
    ProductCategory,
    ProductImage,
    Comment,
    RatingProduct
)

from django.contrib.auth import get_user_model
from apps.authentication.models import (
    SellerAccountModel,
    BuyerAccountModel,
    User
)

class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = ["category_name"]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["product_image"]

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)
    image = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            "id",
            "owner",
            "image",
            "slug",
            "product_name",
            "product_cost",
            "product_quantity",
            "product_description",
            "created_at",
            "updated_at",
            "product_status",
            "discount_price",
        ]
        
    def get_owner(self, obj):
        return {
            "first_name": obj.owner.first_name,
            "last_name": obj.owner.last_name,
            "organization": obj.owner.organization,
            "followers": obj.owner.get_followers_count()
        }
        
    lookup_field = "slug"
    extra_kwargs = {
        "url": {"lookup_field": "slug"}
    }


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    product_name = ProductSerializer()
    class Meta:
        model = Comment
        fields = [
            "user",
            "product_name",
            "comment",
            "created_at",
        ]

        
class RatingProductSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name="product-detail",
        lookup_field="slug",
        queryset=Product.objects.all()
        )
    
    class Meta:
        model = RatingProduct
        fields = ["user", "post", "rating"]
        
class SellerUserSerializer(serializers.HyperlinkedModelSerializer):
    owner_product = serializers.HyperlinkedRelatedField(many=True, view_name="product-detail", lookup_field="slug", queryset=Product.objects.all())
    user = serializers.SerializerMethodField(read_only=True)
    lookup_field = 'first_name'
    extra_kwargs = {
        "url": {"lookup_field": "first_name"}
    }
    
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


    