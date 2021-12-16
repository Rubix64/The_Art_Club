from django.urls import path
from .views import galleries
urlpatterns =[
    path('',galleries,name='galleries')
]