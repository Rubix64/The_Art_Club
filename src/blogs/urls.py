from django.urls import path
from .views import posts,PostDetails,create

urlpatterns = [
   # path('',blog,name="blog"),

   # path('',Blog.as_view(),name="Blog"),
   path('',posts,name='posts'),
   path('post/<int:pk>',PostDetails.as_view(),name="PostDetails"),
   path('create/',create,name="create"),
   # path('uploadform/',upload_form,name="upload"),  
   # path('post/edit/<int:pk>',UpdatePostView.as_view(),name="UpdatePostView")

]




 

