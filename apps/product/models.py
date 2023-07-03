from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars, slugify
from django.contrib import messages

from apps.authentication.models import SellerAccountModel, User

import random

def random_randints(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

# ----------------- Product Category Model ----------------- #
class ProductCategory(models.Model):
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Category'
    
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name
# ----------------- Product Category Model ----------------- #

# ----------------- Product Model ----------------- #
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
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.SET_NULL, related_name='category')

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('base:product_detail', args=[str(self.slug)])
    
    # create average rating for product
    def average_rating(self):
        rating = RatingProduct.objects.filter(post=self).aggregate(models.Avg('rating'))["rating__avg"] or 0
        return rating
    
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
    
    def add_to_cart_url(self):
        return reverse('base:add_to_cart', args=[str(self.slug)])
    
    def remove_from_cart_url(self):
        return reverse('base:remove_from_cart', args=[str(self.slug)])
    
    def remove_single_item_from_cart_url(self):
        return reverse('base:remove_single_item_from_cart', args=[str(self.slug)])
    
# ----------------- Product Model ----------------- #

# ----------------- Product Image Model ----------------- #
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
# ----------------- Product Image Model ----------------- #

# ----------------- Comment Model ----------------- #
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
# ----------------- Comment Model ----------------- #

# ----------------- Rating Product Model ----------------- #
class RatingProduct(models.Model):
    
    class Meta:
        verbose_name = "Rating Product"
        verbose_name_plural = "Rating Products"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.post.product_name}: {self.rating}"
# ----------------- Rating Product Model ----------------- #

#  ----------------- Checkout Item Model ----------------- #
class CheckoutItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"
    
    def get_total_product_cost(self):
        return self.quantity * self.product.product_cost
    
    def get_total_discount_cost(self):
        return self.quantity * self.product.discount_price
    
    def get_amount_saved(self):
        return self.get_total_product_cost() - self.get_total_discount_cost()
    
    def get_last_cost(self):
        if self.product.discount_price:
            return self.get_total_discount_cost()
        return self.get_total_product_cost()
    
#  ----------------- Checkout Item Model ----------------- #
    
# ----------------- Checkout Model ----------------- #
class Checkout(models.Model):
    
    CITIES = (
        ('Tashkent', 'Tashkent'),
        ('Samarkand', 'Samarkand'),
        ('Bukhara', 'Bukhara'),
        ('Khiva', 'Khiva'),
        ('Nukus', 'Nukus'),
        ('Andijan', 'Andijan'),
        ('Namangan', 'Namangan'),
        ('Fergana', 'Fergana'),
        ('Navoi', 'Navoi'),
        ('Urgench', 'Urgench'),
        ('Termez', 'Termez'),
        ('Kokand', 'Kokand'),
    )
    
    class Meta:
        verbose_name = "Checkout"
        verbose_name_plural = "Checkouts"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='checkout')
    checkout_items = models.ManyToManyField(CheckoutItem)
    order_code = models.IntegerField(default=random_randints(8), null=True)
    ordered_date = models.DateTimeField(auto_now_add=True, null=True)
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=998)
    email = models.EmailField()
    post_office = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200, choices=CITIES, default='Tashkent')
    house = models.CharField(max_length=200)
    postal_code = models.IntegerField(default=156876)
    message = models.TextField()
    
    def __str__(self):
        return self.firstname
    
    def get_total(self):
        total = 0
        for checkout_item in self.checkout_items.all():
            total += checkout_item.get_last_cost()
        return total

# ----------------- Checkout Model ----------------- #