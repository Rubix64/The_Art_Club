from django.urls import path
from .views import Blog,PostDetails

urlpatterns = [
   # path('',blog,name="blog"),

   path('',Blog.as_view(),name="Blog"),
   path('post/<int:pk>',PostDetails.as_view(),name="PostDetails"),
   # path('uploadform/',upload_form,name="upload"),  
   # path('post/edit/<int:pk>',UpdatePostView.as_view(),name="UpdatePostView")

]




 

