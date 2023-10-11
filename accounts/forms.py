from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):
    phonenumber = forms.CharField(max_length=15)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter confirmpassword'}))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phonenumber'}))
    
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phonenumber']
    
        if not phonenumber.isdigit() or len(phonenumber)<10 or len(phonenumber)>13:
            raise forms.ValidationError("Given Phone number is invalid...try again")
        return phonenumber   
    
    class  Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2','phonenumber']
       
    def clean_username(self):
        username = self.cleaned_data['username']
        
        if len(username) < 3:
            raise forms.ValidationError("Given username is invalid..try again")
        return username