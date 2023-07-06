from django_unicorn.components import UnicornView
from product.models import Comment
from ..models import User

class CommentsView(UnicornView):
    user: User = None
    comment_model: Comment = None
    comment: str = ""
    
    def mount(self):
        self.user = self.request.user
        return super().mount()