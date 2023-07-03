from django import forms
from django.forms.models import inlineformset_factory
from .models import (
    Product,
    ProductImage,
    Comment,
    RatingProduct,
    Checkout,
)
from apps.authentication.models import SellerAccountModel, User

# create product form class for SellerAccountModel
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_description',
            'product_cost',
            'product_quantity',
            'category',
        ]

    
class ProductImageForm(forms.ModelForm):
    # write code to remove default label
    product_image = forms.ImageField(label='')
    class Meta:
        model = ProductImage
        fields = ('product_image',)

# create a form for comment
class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    class Meta:
        model = Comment
        fields = ('comment',)

# create rating form for product
class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = RatingProduct
        fields = ('rating',)


class CheckoutForm(forms.ModelForm):
    
    CHOICES = [
        ("Express Delivery", "Express Delivery"),
        ("Post Office", "Post Office"),
        ("Pickup", "Pickup"),
    ]
    
    post_office = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = Checkout
        fields = [
            'firstname',
            'lastname',
            'phone_number',
            'post_office',
            'email',
            'address',
            'city',
            'house',
            'postal_code',
            'message',
        ]

# this is for formset for product image
ProductImageFormSet = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=4, can_delete=False)
# this is for update view
ProductImageFormSetUpdate = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=3, can_delete=False)