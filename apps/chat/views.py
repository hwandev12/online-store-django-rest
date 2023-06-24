from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.authentication.models import User, SellerAccountModel
from .forms import MessageForm
from notifications.signals import notify
from notifications.models import Notification

from django.views.generic.edit import FormView

@login_required()
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def message_send_view(request, firstname):
    if request.user.is_buyer:
        seller = SellerAccountModel.objects.get(first_name=firstname)
        form = MessageForm()
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.receiver = seller.user
                form.save()
                notify.send(request.user, recipient=seller.user, verb=form.cleaned_data['content'])
                return redirect('/')
        return render(request, "chat/send-message.html", {"form": form})
    return redirect('/')
    
    
# message_send_view = MessageSendView.as_view()