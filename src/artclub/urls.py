from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from blogs.views import create_post
# from .views import render_home_page
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/',logout_view),
    path('blogs/',include('blogs.urls')),
    path('', index),
    path('prints/',include('prints.urls')),
    path('cart/', include('cart.urls')),
    path('gallery/', include('gallery.urls')),
    # path('',render_home_page),
    path('create/',create_post),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)