from django.shortcuts import render,redirect
from . import forms
from .import models
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def logout_form(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home') 
def login_form(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(email = email)
        except:
            messages.error(request,"user doesn't exist")
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"wrong entry")
    context = {}
    return render(request,"login.html",context)

def home(request):
    posts = models.Post.objects.all()
    channels = models.Channel.objects.all()
    context = {"posts":posts,"channels":channels}
    return render(request,"home.html",context)

def channel(request,pk):

    channel = models.Channel.objects.get(id = pk)
    posts = models.Post.objects.filter(channel__id = pk)
    subscribe = True
    
    if request.user in channel.subscribers.all():
        subscribe = False  
    
    if request.method == 'POST':
        if request.user in channel.subscribers.all():
            channel.subscribers.remove(request.user)
            subscribe = True
        else: 
            channel.subscribers.add(request.user)
            subscribe = False  

    context = {"channel":channel,"posts":posts,"subscribe":subscribe,"subscribers_count":len(channel.subscribers.all())}
    return render(request,'channel.html',context)


def post(request,pk):
    post = models.Post.objects.get(id=pk)
    channel = models.Channel.objects.get(id = post.channel.id)
    likes = True
    dislikes = True
 
    if request.user in post.likes.all():
        likes = False  
    if request.user in post.dislikes.all():
        dislikes = False  
    
    if request.method == 'POST' and 'like' in request.POST:
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            likes = True
        else: 
            post.likes.add(request.user)
            likes = False  
            if request.user in post.dislikes.all():
                post.dislikes.remove(request.user)
                dislikes = True 

    if request.method == 'POST' and 'dislike' in request.POST:
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)
            dislikes = True
        else: 
            post.dislikes.add(request.user)
            dislikes = False  
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                likes = True
 
    
    if request.method == "POST" and 'comment' in request.POST:
        comment = models.Comments.objects.create(  
            user = request.user,
            comment = request.POST.get('comment')
        )
        
        post.comments.add(comment)

   
    likes_count = len(post.likes.all())
    dislikes_count = len(post.dislikes.all())
    comments = post.comments.all()
    context = {"post":post,"comments":comments,"channel":channel,"likes":likes,"dislikes":dislikes,'likes_count':likes_count,'dislikes_count':dislikes_count,'comments_count':len(comments)}

    return render(request,"post.html",context)

@login_required(login_url='login')
def createchannel(request):
    form  = forms.ChannelForm()
    if request.method == "POST":
        form = forms.ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.host = request.user
            form.save()
            return redirect('home') 
    context = {"form":form}   
    return render(request,"createchannel.html",context)

def editchannel(request,pk):
    channel = models.Channel.objects.get(id = pk)
    form  = forms.ChannelForm(instance=channel)
    if request.method == "POST":
        channel.channel_name = request.POST.get('channel_name')
        channel.about_channel = request.POST.get('about_channel')
        channel.save()
        return redirect('home') 
    context = {"form":form}   
    return render(request,"createchannel.html",context)



@login_required(login_url='login')
def createpost(request,pk):
    channel = models.Channel.objects.get(id = pk)
    form  = forms.PostForm()
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.channel = channel
            post.save()
            return redirect('home') 
    context = {"form":form}   
    return render(request,"createpost.html",context)
def editpost(request,pk):
    post = models.Post.objects.get(id = pk)
    form  = forms.PostForm(instance=post)
    if request.method == "POST":
        post.discription = request.POST.get('discription')
        post.title = request.POST.get('title')
        post.save()
        return redirect('home') 
    context = {"form":form}   
    return render(request,"createpost.html",context)

def register(request):
    form = forms.RegisterForm()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    context = {"form":form}
    return render(request,'register_form.html',context)


def delete_channel(request,pk):
    if request.method == "POST":
        channel = models.Channel.objects.get(id = pk)
        if channel.host != request.user:
            return HttpResponse("ACCESS DENIED")
        else:
            channel.delete()
            return redirect('home')
    context = {'context':"surely want to delete this channel"}
    return render(request,'delete.html',context)
def delete_post(request,pk):
    if request.method == "POST":
        post = models.Post.objects.get(id = pk)
        if post.channel.host != request.user:
            return HttpResponse("ACCESS DENIED")
        else:
            post.delete()
            return redirect('home')
    context = {'context':"surely want to delete this post"}
    return render(request,'delete.html',context)
def delete_comment(request,pk):
    
    if request.method == "POST":
        comment = models.Comments.objects.get(id = pk)
        comment.delete()
        q = request.GET.get('q')
        return redirect('post',pk=q)
    context = {'context':"surely want to delete this comment"}
    return render(request,'delete.html',context)
