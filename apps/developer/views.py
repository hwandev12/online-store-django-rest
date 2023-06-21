from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.product.models import Product

class DeveloperHomePage(ListView):
    template_name = 'developer/pages/develop.html'
    context_object_name = 'apps'
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(DeveloperHomePage, self).get_queryset(*args, **kwargs)
        return qs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return super(DeveloperHomePage, self).dispatch(*args, **kwargs)
        else:
            return render(self.request, 'pages/404.html', status=404)


developer_home_page = DeveloperHomePage.as_view()