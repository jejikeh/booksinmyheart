from django.views.generic import ListView, DetailView
from blog.models import blog
from django.urls import path , include
from django.conf.urls import url


urlpatterns = [
    path('', ListView.as_view(queryset=blog.objects.all().order_by("-date")[:20],
    template_name="blog/posts.html")),
    path('<int:pk>/', DetailView.as_view(model=blog, template_name="blog/post.html")),
]
