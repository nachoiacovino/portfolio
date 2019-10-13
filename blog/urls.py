from django.urls import path
from . import views
from .models import Blog

blogs = Blog.objects

urlpatterns = [
    path('', views.allblogs, name="allblogs"),
    path('<int:blog_id>/<slug:slug>/', views.detail, name="detail")
]
