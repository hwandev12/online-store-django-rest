from django.contrib import admin

from .models import Product

# create admin for product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_cost', 'product_quantity', 'short_description', 'product_image')
    list_filter = ('product_name', 'product_cost',)
    # make slug field auto filled
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
