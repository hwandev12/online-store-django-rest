from django.contrib import admin

from .models import Message, ReplyMessage, LiveChatMessage

admin.site.register(Message)
admin.site.register(ReplyMessage)
admin.site.register(LiveChatMessage)