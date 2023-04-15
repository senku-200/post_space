from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required

class User(AbstractUser):
    username = models.CharField(max_length=100,unique = True,null=True,blank=True)
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True)
    avatar   = models.ImageField(upload_to="static/data",null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    comment = models.TextField()
    likes = models.ManyToManyField(User,related_name='comment_likes')
    dislikes = models.ManyToManyField(User,related_name='comment_dislikes')
    created = models.DateTimeField(auto_now=True)    
    updated = models.DateTimeField(auto_now_add=True)    
    class Meta:
        ordering = ["-updated",'-created']

    def __str__(self):
        return self.comment[:50]
class Channel(models.Model):
    channel_name = models.CharField(max_length=100)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User,related_name='subscribers',blank=True)
    about_channel = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)    
    updated = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.channel_name
class Post(models.Model):
    title = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,null=True)
    discription = models.TextField()
    comments = models.ManyToManyField(Comments,related_name='comments',blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='post_likes',blank=True)
    dislikes = models.ManyToManyField(User,related_name='post_dislikes',blank=True)
    created = models.DateTimeField(auto_now=True)    
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ["-updated",'-created']

    def __str__(self):
        return self.title



    


    



    







     
