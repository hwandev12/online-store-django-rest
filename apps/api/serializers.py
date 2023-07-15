from rest_framework import serializers
from apps.product.models import Product, ProductCategory

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    product_name = serializers.CharField(max_length=200)
    product_cost = serializers.IntegerField(default=0)
    product_quantity = serializers.IntegerField()
    product_description = serializers.CharField(max_length=200)
    product_status = serializers.BooleanField(default=True)
    discount_price = serializers.FloatField()
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())
    
    
    def create(self, validated_data):    
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_cost = validated_data.get('product_cost', instance.product_cost)
        instance.product_quantity = validated_data.get('product_quantity', instance.product_quantity)
        instance.product_description = validated_data.get('product_description', instance.product_description)
        instance.product_status = validated_data.get('product_status', instance.product_status)
        instance.discount_price = validated_data.get('discount_price', instance.discount_price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    
    