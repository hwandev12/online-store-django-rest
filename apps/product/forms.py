from django import forms

from .models import Product
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
            'product_image',
        ]
    
    