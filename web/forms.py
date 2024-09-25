from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


#django form
class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=50)
    email = forms.EmailField(label='Email')
    msg = forms.CharField(label='Message', widget=forms.Textarea)

#model form
class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','desc','price','img', 'doc']

#USER CREATION
class UserRegistrationform(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username','password1','password2']


#User Login
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']




