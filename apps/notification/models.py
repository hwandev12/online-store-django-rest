from django.db import models
from apps.authentication.models import User

class Notification(models.Model):
    user_sender = models.ForeignKey(User, related_name='user_sender', on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(User, related_name='user_revoker', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    type_of_notification = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_sender.email
