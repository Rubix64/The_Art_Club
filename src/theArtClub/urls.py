from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from blogs.views import create_post
from .views import render_home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/',include('blogs.urls')),
    path('gallery/',include('gallery.urls')),
    path('',render_home_page),
    path('create/',create_post),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)