from django import forms
from django.forms.models import inlineformset_factory
from .models import Product, ProductImage
from apps.authentication.models import SellerAccountModel

# create product form class for SellerAccountModel
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_cost',
            'product_quantity',
        ]

    
class ProductImageForm(forms.ModelForm):
    # write a multiple image field
    class Meta:
        model = ProductImage
        fields = ('product_image',)

# create formset for product image
ProductImageFormSet = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=3, can_delete=False)