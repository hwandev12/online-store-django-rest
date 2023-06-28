from rest_framework import serializers

from .models import LiveChatMessage

class LiveChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveChatMessage
        fields = '__all__'
        
        def get_sender(self, obj):
            return str(obj.user.email)