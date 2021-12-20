from django.urls import path

from .views import *

urlpatterns =[
    path('',prints,name='Prints'),
    # path('?<search>',prints,name='Prints'),
    path('printdata/',printdata)
]