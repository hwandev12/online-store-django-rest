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
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notifications.models import Notification
from apps.authentication.models import (
    User,
    BuyerAccountModel,
    SellerAccountModel
)
from django.utils.decorators import method_decorator

from apps.chat.models import Message, ReplyMessage
from apps.chat.forms import MessageForm, ReplyMessageForm
from notifications.signals import notify

# ----------------------------------------------------------------------------------- #
@login_required()
def mark_as_read(request, slug=None):
    notification_id = slug2id(slug)
    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    _next = request.GET.get('next')

    if _next and url_has_allowed_host_and_scheme(_next, settings.ALLOWED_HOSTS):
        return redirect(iri_to_uri(_next))

    return redirect("authentication:single_notification", pk=Notification.objects.get(id=notification_id).id)
# ----------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------- #
class SingleNotificationView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = 'notifications/sellers/single.html'
    context_object_name = 'notification'

    def get_object(self, queryset=None):
        notification = super(SingleNotificationView, self).get_object(queryset=queryset)
        if notification.recipient == self.request.user:
            return notification
        else:
            return redirect('/')
        
    def get_context_data(self, **kwargs):
        context = super(SingleNotificationView, self).get_context_data(**kwargs)
        context['notifications_count'] = self.request.user.notifications.count()
        context['notification'] = self.get_object()
        return context

# ----------------------------------------------------------------------------------- #
class NotificationViewList(ListView):
    template_name = 'notifications/sellers/list.html'
    context_object_name = 'notifications'

    def get_notifications_by_paginator(self):
        paginate = Paginator(self.get_queryset(), 10)
        page_number = self.request.GET.get('page')
        notification_page_obj = paginate.get_page(page_number)
        return notification_page_obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_seller:
            return super(NotificationViewList, self).dispatch(request, *args, **kwargs)
        # later on we will add a 404 page
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super(NotificationViewList, self).get_context_data(**kwargs)
        context['notifications'] = self.get_notifications_by_paginator()
        context['notifications_count'] = self.request.user.notifications.count()
        context['notifications_count_unread'] = self.request.user.notifications.unread().count()
        return context
# ----------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------- #
class AllNotificationsList(NotificationViewList):
    """
    Index page for authenticated user
    """

    def get_queryset(self):
        if self.request.user.is_seller:
            if notification_settings.get_config()['SOFT_DELETE']:
                qset = self.request.user.notifications.active()
            else:
                qset = self.request.user.notifications.all()
            return qset
        return redirect('/')
    
# ----------------------------------------------------------------------------------- #
class UnreadNotificationsList(ListView):                                              # 
    """                                                                               # 
    Unread notifications page for authenticated user                                  #           
    """                                                                               #      
    template_name = 'notifications/sellers/unread.html'                                       #
    context_object_name = 'notifications_unread'                                      #                   
                      
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_seller:
            return super(UnreadNotificationsList, self).dispatch(request, *args, **kwargs)
        # later on we will add a 404 page
        return redirect('/')                      
                                                                                      #
    def get_queryset(self):                                                           #
        if notification_settings.get_config()['SOFT_DELETE']:                         #
            qset = self.request.user.notifications.unread().active()                  #
        else:                                                                         #
            qset = self.request.user.notifications.unread()                           #
        return qset                                                                   #                                   
                                                                                      #
    def get_context_data(self, **kwargs):                                             # 
        context = super(UnreadNotificationsList, self).get_context_data(**kwargs)     #
        context['notifications_unread'] = self.get_queryset()                         #
        # get all notifications count                                                 #
        context['notifications_count'] = self.request.user.notifications.count()      #
        return context                                                                #                                                                         #
# ----------------------------------------------------------------------------------- #
    
# ----------------------------------------------------------------------------------- #
class SentMailView(LoginRequiredMixin, ListView):
    template_name = 'notifications/sellers/sent.html'
    context_object_name = 'sent_mail'
    
    def get_queryset(self):
        return ReplyMessage.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(SentMailView, self).get_context_data(**kwargs)
        context['sent_mail'] = self.get_queryset()
        context['notifications_count'] = self.request.user.notifications.count()
        return context
# ----------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------- #
@login_required
def mark_all_as_read(request):
    request.user.notifications.mark_all_as_read()

    _next = request.GET.get('next')

    if _next and url_has_allowed_host_and_scheme(_next, settings.ALLOWED_HOSTS):
        return redirect(iri_to_uri(_next))
    return redirect('authentication:all_notifications')
# ----------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------- #
all_notifications = AllNotificationsList.as_view()
single_notification = SingleNotificationView.as_view()
unread_notifications = UnreadNotificationsList.as_view()
sent_mail = SentMailView.as_view()
# ----------------------------------------------------------------------------------- #