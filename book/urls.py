from django.views.generic import ListView, DetailView
from book.models import book
from django.urls import path , include
from django.conf.urls import url


urlpatterns = [
    path('', ListView.as_view(queryset=book.objects.all().order_by("-date")[:20],
    template_name="book/books.html")),
    path('<int:pk>/', DetailView.as_view(model=book, template_name="book/book.html")),
]
