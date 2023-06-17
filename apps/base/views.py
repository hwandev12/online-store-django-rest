from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse
from apps.product.models import (
    Product,
    ProductImage,
    ProductCategory,
    Comment
)
from apps.product.forms import (
    ProductForm,
    ProductImageForm,
    ProductImageFormSet,
    ProductImageFormSetUpdate,
    CommentForm
)
from django.db import transaction
from apps.authentication.models import SellerAccountModel
from django.contrib import messages
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # create a method to get all products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:3]
        context["latest_products_for_product_page"] = Product.objects.all().order_by('-created_at')[:10]
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        if not self.request.user.is_seller:   
            context['form'] = CommentForm()
        context['comments'] = self.object.comment.all()
        # get comments by owner of the comment
        context['comments_by_owner'] = self.object.comment.filter(user=self.request.user)
        return context
    
    # write a post method to add comment
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_seller:
            if self.request.method == 'POST':
                form = CommentForm(self.request.POST)
                if form.is_valid():
                    comment = form.cleaned_data.get('comment') 
                
                new_comment = Comment(comment=comment, product_name=self.get_object(), user=self.request.user)
                new_comment.save()
                return redirect('base:product_detail', slug=self.kwargs['slug'])
        else:
            pass
    
# create a function to delete comment only owner can delete comment
def delete_comment(request, slug, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('base:product_detail', slug=slug)
    
# create product create class
class ProductCreateView(CreateView):
    template_name = 'pages/product_create.html'
    form_class = ProductForm
    
    # create method to allow only seller to create product
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_seller:
            # later on i would add 404 page here
            return redirect('base:home')
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context["product_image"] = ProductImageFormSet()
        if self.request.POST:
            context['product_image'] = ProductImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['product_image'] = ProductImageFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        product_image = context["product_image"]
        with transaction.atomic():
            form.instance.owner = self.request.user.selleraccountmodel
            self.object = form.save()
            if product_image.is_valid():
                product_image.instance = self.object
                product_image.save()
        form.instance.owner = self.request.user.selleraccountmodel
        return super(ProductCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('base:product_detail', args=[self.object.slug])
    
class ProductDeleteVeiew(DeleteView):
    model = Product
    template_name = 'pages/product_delete.html'
    context_object_name = 'product'
    
    def get_success_url(self):
        return reverse('base:home')
    
    # create method to allow only seller to delete product
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_seller:
            # later on i would add 404 page here
            return redirect('base:home')
        return super().dispatch(*args, **kwargs)
    
    # create a method only allow owner to delete product
    def get_object(self, queryset=None):
        product = super(ProductDeleteVeiew, self).get_object()
        if not product.owner == self.request.user.selleraccountmodel:
            return redirect('base:home')
        return product
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('base:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['slug'])
        return context
    
# create a class to update product
class ProductUpdate(UpdateView):
    template_name = 'pages/product_update.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    
    # create method to allow only seller to update product
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_seller:
            # later on i would add 404 page here
            return redirect('base:home')
        return super().dispatch(*args, **kwargs)
    
    # update product image
    def get_context_data(self, **kwargs):
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        context["product_image"] = ProductImageFormSetUpdate(instance=self.object)
        if self.request.POST:
            context['product_image'] = ProductImageFormSetUpdate(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['product_image'] = ProductImageFormSetUpdate(instance=self.object)
        return context
    
    # create a method only allow owner to update product
    def get_object(self, queryset=None):
        product = super(ProductUpdate, self).get_object()
        if not product.owner == self.request.user.selleraccountmodel:
            return redirect('base:home')
        return product
    
    # write form valid method
    def form_valid(self, form):
        context = self.get_context_data()
        product_image = context["product_image"]
        with transaction.atomic():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            form.instance.owner = self.request.user.selleraccountmodel
            self.object = form.save()
            if product_image.is_valid():
                product_image.instance = self.object
                product_image.save()
        form.instance.owner = self.request.user.selleraccountmodel
        return super(ProductUpdate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('base:product_detail', args=[self.object.slug])

class WelcomePage(TemplateView):
    template_name = 'components/welcome_choose.html'
    
    
# create not found page class view
# class NotFound(TemplateView):
#     template_name = 'pages/not_found.html'
    
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# make classes to functionable
home_page_view = HomePageView.as_view()
welcome_page = WelcomePage.as_view()
# create a function name from class
product_detail_view = ProductDetailView.as_view()
product_create_view = ProductCreateView.as_view()
product_delete_view = ProductDeleteVeiew.as_view()
product_update_view = ProductUpdate.as_view()