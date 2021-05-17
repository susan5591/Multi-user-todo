from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm

from .models import TODO

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','task','status','priority']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']