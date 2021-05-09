from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    boi = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile_pic")
    website_url = models.CharField(max_length=250,null=True,blank=True)
    facebook_url = models.CharField(max_length=250,null=True,blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=250)
    image_header = models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    snippets = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank='True',null='True')
    post_data = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

    