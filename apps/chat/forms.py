from django import forms
from .models import Message, ReplyMessage
from apps.authentication.models import User

class MessageForm(forms.ModelForm):
    
    TITLES = (
        ("Shikoyat", "Shikoyat"),
        ("Taklif", "Taklif"),
        ("Savol", "Savol"),
    )
    
    title = forms.ChoiceField(choices=TITLES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Message
        fields = ['content', 'title']
        
class ReplyMessageForm(forms.ModelForm):
    class Meta:
        model = ReplyMessage
        fields = ['content']