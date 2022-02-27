from apps.user.models import User
from django.views.generic.edit import CreateView


class UserRegistrationView(CreateView):
    model = User
    fields = ('username', 'password',)
    template_name = 'register.html'
