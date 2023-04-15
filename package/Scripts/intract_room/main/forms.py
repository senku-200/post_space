from django.forms import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username','firstname','lastname','email',"password1","password2","avatar","about"]


class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
        exclude = ["comments",'channel','likes','dislikes']
class ChannelForm(ModelForm):
    class Meta:
        model = models.Channel
        fields = ['channel_name','about_channel']
        exclude = ["post"]
        
class CommentForm(ModelForm):
    class Meta:
        model = models.Comments
        fields = "__all__"
        exclude = ['likes','dislikes']
