from django.db.models.signals import post_save
from notifications.signals import notify
from apps.chat.models import Message

def message_notification(sender, instance, created, **kwargs):
    notify.send(instance.user, recipient=instance.user, verb='sent you a message', action_object=instance, description=instance.content)
        
post_save.connect(message_notification, sender=Message)