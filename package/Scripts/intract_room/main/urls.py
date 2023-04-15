from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path("register",views.register,name = "register"),
    path("createchannel",views.createchannel,name='createchannel'),
    path("createpost/<str:pk>/",views.createpost,name = "createpost"),
    path("post/<str:pk>/",views.post,name="post"),
    path("channel/<str:pk>/",views.channel,name="channel"),
    path("login",views.login_form,name="login"),
    path("logout",views.logout_form,name="logout"),
    path("delete_channel/<str:pk>/",views.delete_channel,name="delete_channel"),
    path("delete_post/<str:pk>/",views.delete_post,name="delete_post"),
    path("delete_comment/<str:pk>/",views.delete_comment,name="delete_comment"),
    path("editchannel/<str:pk>/",views.editchannel,name="editchannel"),
    path("editpost/<str:pk>/",views.editpost,name="editpost"),
]
