from django.views.generic import ListView, DetailView
from mainApp.models import news
from django.urls import path, include
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=news.objects.all().order_by("-date")[:20],
    template_name="mainApp/index.html")),
    path('contact/', views.contact, name='contact'),
]
