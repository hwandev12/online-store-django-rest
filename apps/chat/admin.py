from django.contrib import admin

from .models import Message, ReplyMessage

admin.site.register(Message)
admin.site.register(ReplyMessage)