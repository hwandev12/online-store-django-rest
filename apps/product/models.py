from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars, slugify

from apps.authentication.models import SellerAccountModel

# create model for product with product_name, product_cost, product_quantity, product_description, product_image
class Product(models.Model):
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
    
# create model for product image with product_image
class ProductImage(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='image')
    product_image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.product.product_name
    
    def get_absolute_url(self):
        return reverse('base:product_detail', args=[str(self.product.slug)])
    
