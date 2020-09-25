from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="First Name",required=True)
    last_name = forms.CharField(label="Last Name",required=True)
    email = forms.EmailField(label="Email",required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','image']