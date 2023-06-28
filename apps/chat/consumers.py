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

class LiveChatConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    
    queryset = LiveChatMessage.objects.all()
    serializer_class = LiveChatMessageSerializer
    permission_classes = (permissions.AllowAny,)
    
    async def connect(self, **kwargs):
        await self.livechatmessage_consumer_change.subscribe()
        await super().connect(**kwargs)
    
    @model_observer(LiveChatMessage)
    async def livechatmessage_consumer_change(self, message, observer=None, **kwargs):
        await self.send_json(message)
        
    @livechatmessage_consumer_change.serializer
    def livechatmessage_model_serializer(self, instance, action, **kwargs):
        return dict(data=LiveChatMessageSerializer(instance=instance).data, action=action.value)

# -------------------------------------------------------- #


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

        # await save_message(message, self.scope["user"])
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
 
# @database_sync_to_async
# def save_message(message, user):
#     return LiveChatMessage.objects.create(user=user, content=message)

# -------------------------------------------------------- #

