from django_unicorn.components import UnicornView
from apps.product.models import Comment, Product
from apps.authentication.models import User

class CommentsView(UnicornView):
    user: User = None
    product_name: Product = None
    comment_model: Comment = None
    comment: str = ""
    
    def mount(self):
        self.user = self.request.user
        self.comment_model = Comment.objects.filter(product_name=self.product_name)
        return super().mount()
    
    def submit(self):
        Comment.object.create(
            user=self.user,
            comment=self.comment
        )
        
        self.comment = ""
        self.comment_model = Comment.objects.all()