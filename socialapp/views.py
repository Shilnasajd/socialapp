from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from socialapp.forms import RegistrationForm,LoginForm,PostsForm,UserProfileForm
from django.views.generic import View,CreateView,FormView,ListView,TemplateView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages
from socialapp.models import Posts,Comments,UserProfile

# Create your views here.


class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name: str="register.html"
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        # messages.success(request,"REGISTRATION COMPLETED SUCCESSFULLY")
        return super().form_valid(form)

class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password") 
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                messages.success(request,"LOGIN COMPLETED SUCCESSFULLY")
                return redirect("home")
            else:
                messages.error(request,"LOGIN FAILED")
                return render(request,self.template_name,{"form":form})

class HomeView(CreateView):
    template_name: str="home.html"
    model=Posts
    form_class=PostsForm
    success_url=reverse_lazy("home")
    context_object_name="posts"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form) 


class PostList(ListView):
    template_name="allposts.html"
    model=Posts
    context_object_name="posts"

    def get_queryset(self):
        return Posts.objects.all().exclude(user=self.request.user)

def add_comment(request,*args,**kwargs):
    p_id=kwargs.get("id") 
    pst=Posts.objects.get(id=p_id)
    cmt=request.POST.get("comment")  
    pst.comments_set.create(comment=cmt,user=request.user)
    messages.success(request,"COMMENT ADDED SUCCESS")
    return redirect("home") 

def add_commentlikes(request,*args,**kwargs):
    cmt_id=kwargs.get("id")
    cmt=Comments.objects.get(id=cmt_id)
    cmt.cmt_likes.add(request.user)
    cmt.save()
    messages.success(request,"ADDED COMMENT LIKES SUCCESS")
    return redirect("home")

def post_likes(request,*args,**kwargs):
    pst_id=kwargs.get("id")
    pst=Posts.objects.get(id=pst_id)
    pst.likes.add(request.user)
    pst.save()
    messages.success(request,"ADDED LIKES SUCCESS")
    return redirect("home")

class MyPosts(ListView):
    model=Posts
    template_name="myposts.html"
    context_object_name="posts"

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

def sign_out(request,*args,**kwargs):
    logout(request)
    messages.success(request,"LOGOUT SUCCESSFULLY")
    return redirect("signin")

def post_delete(request,*args,**kwargs):
    pst_id=kwargs.get("id")
    Posts.objects.filter(id=pst_id).delete()
    messages.success(request,"POST DELETED SUCCESSFULLY")
    return redirect("myposts")
    
class MyProfile(CreateView,ListView):
    template_name: str="myprofile.html"
    model=UserProfile
    form_class=UserProfileForm
    success_url=reverse_lazy("myprofile")
    context_object_name="myprofile"

    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)