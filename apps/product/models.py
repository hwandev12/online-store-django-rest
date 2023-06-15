from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars

from apps.authentication.models import SellerAccountModel

# create model for product with product_name, product_cost, product_quantity, product_description, product_image
class Product(models.Model):
    owner = models.ForeignKey(SellerAccountModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_cost = models.IntegerField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
    
    # create a method to truncate product_description to 50 characters
    @property
    def short_description(self):
        return truncatechars(self.product_description, 50)
    
