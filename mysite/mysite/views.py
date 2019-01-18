from django.views.generic import TemplateView

# 아래 3줄 추가
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# Homepage View
class HomeView(TemplateView):
    template_name = "home.html"

# 다음 내용 추가
#  User Creation
class UserCreateView(CreateView):
    template_name='registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = "registration/register_done.html"
    
