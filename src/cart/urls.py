from django.urls import path

from .views import *

urlpatterns =[
    path('',cart,name='Cart'),
    path('cartadd/',cartadd),
    path('cartremove/',cartremove),
    path('cartdelete/',cartdelete),
]