from django.urls import path
from .views import *
urlpatterns =[
    path('',galleries,name='galleries'),
    path('gallerydata/',gallerydata,name="gallarydata")
]