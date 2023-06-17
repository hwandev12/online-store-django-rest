from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars, slugify
from django.contrib import messages

from apps.authentication.models import SellerAccountModel, User

class ProductCategory(models.Model):
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Category'
    
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
        
    # add slug field
    slug = models.SlugField(max_length=200, unique=True, null=True)
    owner = models.ForeignKey(SellerAccountModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_cost = models.IntegerField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    product_status = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL, related_name='category')

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('base:product_detail', args=[str(self.slug)])
    
    # create a method to create slug from product_name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    
    # create a method to truncate product_description to 50 characters
    @property
    def short_description(self):
        return truncatechars(self.product_description, 50)
    
    # create a method to convert product_cost to uzs
    @property
    def uzs_cost(self):
        return f"{self.product_cost:,} 000 UZS"
    
    # create a method to get product_image
    def get_image(self):
        return self.image.all()[1:]
    # write a code to get first image from ProductImage model
    def get_first_image(self):
        if self.image.first():
            return self.image.first().get_product_image_url()
    
    # create a method to get product_quantity
    @property
    def get_quantity(self):
        return self.product_quantity
    
    # create a method to get product_status
    @property
    def get_status(self):
        return self.product_status
    
    # create a method to get product_cost
    @property
    def get_cost(self):
        return self.product_cost

    
# create model for product image with product_image
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    product_image = models.ImageField(upload_to='products/')
    
    
    def __str__(self):
        return self.product.product_name
    
    # create method product only created 4 times allow update
    def save(self, *args, **kwargs):
        if not self.pk and self.product.image.count() >= 4:
            return reverse('base:product_detail', args=[str(self.product.slug)])
        return super().save(*args, **kwargs)
    
    def get_product_image_url(self):
        return self.product_image.url
    
    def get_absolute_url(self):
        return reverse('base:product_detail', args=[str(self.product.slug)])

class Comment(models.Model):
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email