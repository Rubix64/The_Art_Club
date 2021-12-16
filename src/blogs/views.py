from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView,DetailView,UpdateView
from .models import Post

# def blog(request):
#     return render(request,'blogpage.html')

# def upload_form(request):
#         return render(request, 'blogUploadForm.html')

def create_post(request):
    if request.method == 'POST':
        author=request.POST['author']
        title=request.POST['title']
        image=request.FILES['image']
        description=request.POST['description']
        content=request.POST['content']
        posts=Post(author=author, title=title, image=image, description=description, content=content)
        posts.save()
        return render(request,'uploadsuccess.html')

class Blog(ListView):
    model=Post
    template_name="blogdisplay.html"

class PostDetails(DetailView):
    model=Post
    template_name='blogdetails.html'




    