from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import SellerAccountModel

class ProfileSignupView(SignupView):
    
  template_name = 'account/seller_register.html'
  success_url = '/'  
  form_class = SignupForm
  profile_class = None  # profile class goes here

  def form_valid(self, form):
    response = super(ProfileSignupView, self).form_valid(form)
    profile = self.profile_class(user=self.user)
    profile.save()

    return response