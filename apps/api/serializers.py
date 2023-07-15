from rest_framework import serializers
from apps.product.models import Product, ProductCategory, ProductImage

class ProductImageSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = "__all__"
    
    
    