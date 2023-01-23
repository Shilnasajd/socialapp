from cProfile import label
from operator import attrgetter
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from socialapp.models import Posts,UserProfile

from django import forms

class RegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="USERNAME")

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD1")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD2")
    firstname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="First NAME")
    lastname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="LAST NAME")
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="EMAIL")

    class Meta:
        model=User
        

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="USERNAME")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD")
    class Meta:
        model=User
       
    

class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["post","image"]
        widgets={
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }
        labels={
            "post":"POST",
            "image":"IMAGE",
        }
class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["address","dob","pro_pic","gender"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control","rows":2}),
            "dob":forms.DateInput(attrs={"class":"form-control"}),
            "pro_pic":forms.FileInput(attrs={"class":"form-control"}),
            "gender":forms.TextInput(attrs={"class":"form-control"}),
        }
        labels={
            "address":"ADDRESS",
            "dob":"DOB",
            "pro_pic":"PROFILE PICTURE",
            "gender":"GENDER",
        }