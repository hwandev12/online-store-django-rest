from django.contrib import admin

from .models import (
    Product,
    ProductImage,
    ProductCategory,
    Comment,
    RatingProduct,
    Checkout,
    CheckoutItem
)
# create admin for product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_quantity', 'short_description')
    list_filter = ('product_name',)
    # make slug field auto filled
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Comment)
admin.site.register(RatingProduct)
admin.site.register(Checkout)
admin.site.register(CheckoutItem)
