from django.db import models
from apps.authentication.models import User


# create message model
class Message(models.Model):
    user = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email

    # return last 20 messages
    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]

