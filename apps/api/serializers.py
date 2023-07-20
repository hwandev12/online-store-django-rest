from rest_framework import serializers
from apps.product.models import (
    Product,
    ProductCategory,
    ProductImage,
    Comment,
    RatingProduct,
    CheckoutItem,
    Checkout
)

from django.contrib.auth import get_user_model
from apps.authentication.models import (
    SellerAccountModel,
    BuyerAccountModel,
    User,
    BuyerProfile,
    SellerProfile,
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
        
class CheckoutItemProductSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name="product-detail",
        lookup_field="slug",
        queryset=Product.objects.all()
    )
    
    cart_user_data = serializers.SerializerMethodField(read_only=True)    
    class Meta:
        model = CheckoutItem
        fields = ["cart_user_data", "ordered", "product", "quantity"]
        
    def get_cart_user_data(self, obj):
        return {
            "Email": obj.user.email,
            "Total Cost": f"${obj.get_total_product_cost()}",
        }
        
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name="product-detail",
        lookup_field='slug',
        queryset=Product.objects.all()
    )
    
    user_data = serializers.SerializerMethodField()
    user = serializers.HyperlinkedIdentityField(view_name='buyer-detail')
    
    class Meta:
        model = Checkout
        fields = [
            "user_data",
            "user",
            "product",
            "order_code",
            "ordered_date",
            "ordered",
            "being_delivered",
            "received",
            "firstname",
            "lastname",
            "phone_number",
            "email",
            "post_office",
            "address",
            "city",
            "house",
            "postal_code",
            "message"
        ]
        
    def get_user_data(self, obj):
        return {
            "Email": obj.user.user.email,
            "First Name": obj.user.first_name
        }
        
        
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
        
    lookup_field = 'first_name'
    extra_kwargs = {
        "url": {"lookup_field": "first_name"}
    }

class AllUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

# create a serializer for users that: buyer | seller

class BuyerProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.HyperlinkedIdentityField(view_name="buyer-detail", lookup_field="first_name")
    
    class Meta:
        model = BuyerProfile
        fields = ["user", "avatar"]
        
    lookup_field = 'first_name'
    extra_kwargs = {
        "url": {"lookup_field": "first_name"}
    }

    