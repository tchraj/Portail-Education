from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username', 'email','password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']

class DateInput(forms.DateInput):
    input_type = 'date'
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homeworks
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']
class DashbordForm(forms.Form):
    text = forms.CharField(max_length = 100,label="Enter Your search:")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']

    

