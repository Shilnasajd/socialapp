from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
  # caption=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    likes=models.ManyToManyField(User,related_name="likes")

    @property
    def fetch_comments(self):
        comments=self.comments_set.all()
        return comments

    def __str__(self):
        return self.post

class Comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    cmt_likes=models.ManyToManyField(User,related_name="upvotes")

    def __str__(self):
        return self.comment

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    dob=models.DateField()
    pro_pic=models.ImageField(upload_to="images")
    gender=models.CharField(max_length=100)
