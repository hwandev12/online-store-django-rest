from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from notifications.utils import id2slug, slug2id
from notifications import settings as notification_settings
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.encoding import iri_to_uri

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notifications.models import Notification
from apps.authentication.models import (
    User,
    BuyerAccountModel,
    SellerAccountModel
)

@login_required()
def mark_as_read(request, slug=None):
    notification_id = slug2id(slug)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    _next = request.GET.get('next')

    if _next and url_has_allowed_host_and_scheme(_next, settings.ALLOWED_HOSTS):
        return redirect(iri_to_uri(_next))

    return redirect("authentication:single_notification", pk=notification_id)


class SingleNotificationView(DetailView):
    model = Notification
    template_name = 'notifications/single.html'
    context_object_name = 'notification'

    def get_object(self, queryset=None):
        notification = super(SingleNotificationView, self).get_object(
            queryset=queryset)
        if notification.recipient == self.request.user:
            return notification
        else:
            return redirect('/')
        
    def get_context_data(self, **kwargs):
        context = super(SingleNotificationView, self).get_context_data(**kwargs)
        context['notification'] = Notification.objects.get(id=self.kwargs['pk'])
        return context
    
single_notification = SingleNotificationView.as_view()