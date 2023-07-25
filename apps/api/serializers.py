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

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token


# remove default username field from buyer and seller registration
class CustomUserLoginSerializer(LoginSerializer):
    username = None 

# create a serializer to register user as buyer and seller in order
class SellerUserRegisterSerializer(RegisterSerializer):
    username = None
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.IntegerField(default=998)
    organization = serializers.CharField()
    
    def get_cleaned_data(self):
        data = super(SellerUserRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
            "organization": self.validated_data.get("organization", "")
        }
        data.update(extra_data)
        return data
    
    def save(self, request):
        user = super(SellerUserRegisterSerializer, self).save(request)
        user.is_seller = True
        user.save()
        seller = SellerAccountModel(
            user=user,
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            phone_number=self.cleaned_data.get("phone_number"),
            organization=self.cleaned_data.get("organization")
        )
        seller.save()
        return user
    
class BuyerUserRegisterSerializer(RegisterSerializer):
    username = None
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.IntegerField(default=998)
    company = serializers.CharField()
    
    def get_cleaned_data(self):
        data = super(BuyerUserRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
            "company": self.validated_data.get("company", "")
        }
        data.update(extra_data)
        return data
    
    def save(self, request):
        user = super(BuyerUserRegisterSerializer, self).save(request)
        user.is_buyer = True
        user.save()
        buyer = BuyerAccountModel(
            user=user,
            first_name=self.cleaned_data.get("first_name"),
            last_name=self.cleaned_data.get("last_name"),
            phone_number=self.cleaned_data.get("phone_number"),
            company=self.cleaned_data.get("company"),
        )
        buyer.save()
        return user

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
    product_name = serializers.HyperlinkedRelatedField(
        lookup_field="slug",
        view_name="api-product-detail",
        queryset=Product.objects.all()
    )
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
        view_name="api-product-detail",
        lookup_field="slug",
        queryset=Product.objects.all()
        )
    
    class Meta:
        model = RatingProduct
        fields = ["user", "post", "rating"]
        
class CheckoutItemProductSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name="api-product-detail",
        lookup_field="slug",
        queryset=Product.objects.all()
    )
    
    cart_user_data = serializers.SerializerMethodField(read_only=True)    
    class Meta:
        model = CheckoutItem
        fields = ["cart_user_data", "ordered", "product", "quantity"]
        
    def get_cart_user_data(self, obj):
        return {
            "Email": obj.user.user.email,
            "Total Cost": f"${obj.get_total_product_cost()}",
        }

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name="api-product-detail",
        lookup_field='slug',
        queryset=Product.objects.all()
    )
    
    user_data = serializers.SerializerMethodField()
    user = serializers.HyperlinkedRelatedField(
        view_name="buyer-detail",
        lookup_field="first_name",
        queryset=BuyerAccountModel.objects.all()
    )
    
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
        
# create a serializer for users that: buyer | seller

class BuyerProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.HyperlinkedRelatedField(
        view_name="buyer-detail",
        lookup_field="first_name",
        queryset=BuyerAccountModel.objects.all()
    )
    
    class Meta:
        model = BuyerProfile
        fields = ["user", "avatar"]
    
class SellerProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name="seller-detail",
        lookup_field="first_name",
        queryset=SellerAccountModel.objects.all()
    )
    class Meta:
        model = SellerProfile
        fields = ["user", "avatar"]
        
class SellerUserSerializer(serializers.HyperlinkedModelSerializer):
    owner_product = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="api-product-detail",
        lookup_field="slug",
        queryset=Product.objects.all()
    )
    seller_profile = SellerProfileSerializer()
    user = serializers.SerializerMethodField(read_only=True)
    lookup_field = 'first_name'
    extra_kwargs = {
        "url": {"lookup_field": "first_name"}
    }
    
    class Meta:
        model = SellerAccountModel
        fields = ['id', 'user', 'seller_profile', 'first_name', 'last_name', 'phone_number', 'organization', 'owner_product']
        
    # write a method to get user information
    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "email": obj.user.email,
            "is_staff": obj.user.is_staff,
            "is_superuser": obj.user.is_superuser,
            "is_active": obj.user.is_active
        }
        
    def update(self, instance, validated_data):
        seller_profile_data = validated_data.pop("seller_profile")
        seller_profile = instance.seller_profile
        
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.organization = validated_data.get("organization", instance.organization)
        instance.save()
        
        seller_profile.avatar = seller_profile_data.get(
            'avatar',
            seller_profile.avatar
        )
        seller_profile.save()
        return instance
class BuyerUserSerializer(serializers.ModelSerializer):
    buyer_profile = BuyerProfileSerializer()
    class Meta:
        model = BuyerAccountModel
        fields = "__all__"
        
    lookup_field = 'first_name'
    extra_kwargs = {
        "url": {"lookup_field": "first_name"}
    }

    def update(self, instance, validated_data):
        
        buyer_profile_data = validated_data.pop('buyer_profile')
        buyer_profile = instance.buyer_profile
        
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.company = validated_data.get("company", instance.company)
        instance.save()
        
        buyer_profile.avatar = buyer_profile_data.get(
            'avatar',
            buyer_profile.avatar
        )
        
        buyer_profile.save()
        return instance
        
        
    

class AllUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

