from django.urls import path
from .views import Blog, Notification



urlpatterns = [
    path("",Blog.as_view(),name="home"),
    path("notification/",Notification.as_view(),name="notification")
]