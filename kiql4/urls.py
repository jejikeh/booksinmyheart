from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('blog/', include('blog.urls')),
    path('book/',include('book.urls')),
]
