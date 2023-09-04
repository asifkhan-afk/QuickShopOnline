from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import  password_validation
from.models import Customer


class UserSignup(UserCreationForm):
    password1 = forms.CharField(max_length=40,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=40,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(max_length=40, label='Email',required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())


class changepassword(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'form-control'}))
    new_password1=forms.CharField(
        label=("New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'form-control'}))
    new_password2=forms.CharField(
        label=("Conform Password"),
            strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))


class ResetPassword(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','form':'form-control'}) )

class ResetPAsswordset(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )
class Customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','city','locality','zipcode','state']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.TextInput(attrs={'class':'form-control'}),
                 'locality':forms.TextInput(attrs={'class':'form-control'}),
                 'state':forms.Select(attrs={'class':'form-control'}),
                 'zipcode':forms.NumberInput(attrs={'class':'form-control'}),

                 }