from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from notifications.utils import id2slug, slug2id
from notifications import settings as notification_settings
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.encoding import iri_to_uri

from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notifications.models import Notification
from apps.authentication.models import (
    User,
    BuyerAccountModel,
    SellerAccountModel
)
from django.utils.decorators import method_decorator

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
    
class NotificationViewList(ListView):
    template_name = 'notifications/list.html'
    context_object_name = 'notifications'
    
    def get_notifications_by_paginator(self):
        paginate = Paginator(self.get_queryset(), 10)
        page_number = self.request.GET.get('page')
        notification_page_obj = paginate.get_page(page_number)
        return notification_page_obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NotificationViewList, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NotificationViewList, self).get_context_data(**kwargs)
        context['notifications'] = self.get_notifications_by_paginator()
        context['notifications_count'] = self.request.user.notifications.count()
        context['notifications_count_unread'] = self.request.user.notifications.unread().count()
        return context

class AllNotificationsList(NotificationViewList):
    """
    Index page for authenticated user
    """

    def get_queryset(self):
        if notification_settings.get_config()['SOFT_DELETE']:
            qset = self.request.user.notifications.active()
        else:
            qset = self.request.user.notifications.all()
        return qset
    
all_notifications = AllNotificationsList.as_view()
single_notification = SingleNotificationView.as_view()