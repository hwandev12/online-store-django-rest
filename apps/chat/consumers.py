# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import (
    LiveChatMessage
)

from .serializers import LiveChatMessageSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions

# -------------------------------------------------------- #
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        email = text_data_json["email"]

        # await save_message(message, self.scope["user"])
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "email": email,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        email = event["email"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "email": email}))
 
# @database_sync_to_async
# def save_message(message, user):
#     return LiveChatMessage.objects.create(user=user, content=message)

# -------------------------------------------------------- #

