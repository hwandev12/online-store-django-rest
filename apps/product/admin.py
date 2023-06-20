from django.contrib import admin

from .models import (
    Product,
    ProductImage,
    ProductCategory,
    Comment,
    RatingProduct
)
# create admin for product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'uzs_cost', 'product_quantity', 'short_description')
    list_filter = ('product_name', 'product_cost',)
    # make slug field auto filled
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Comment)
admin.site.register(RatingProduct)
