from django.shortcuts import redirect,render
from django.template import RequestContext
from django.views.generic import ListView,DetailView,UpdateView
from .models import Post
from .forms import BlogForm
from django.http import JsonResponse
# def blog(request):
#     return render(request,'blogpage.html')

# def upload_form(request):
#         return render(request, 'blogUploadForm.html')
from cart.views import no_of_contents
# def create(request):
#     if request.method == 'POST':
#         # print(author_first_name)
#         author=request.POST.get('author',request.user)
#         # print(author.first_name)
#         title=request.POST['title']
#         image=request.FILES['image']
#         description=request.POST['description']
#         content=request.POST['content']
#         posts=Post(author=author, title=title, image=image, description=description, content=content)
#         posts.save()
#         return redirect('/blogs/')

# class Blog(ListView):
#     model=Post
#     template_name="blogdisplay.html"

def posts(request):
    context={}
    context['no_of_contents']= no_of_contents(request.user) 
    if(Post.objects.count() == 0):
        context['nodata']=True 
    else:
        if request.method == 'GET' and request.GET.get('authorsearch'):
            authorsearch = request.GET.get('authorsearch')
            context['posts']=Post.objects.filter(author__first_name__icontains=authorsearch).order_by('-date') 
            if(context['posts'].count() == 0):
                context['nodata']=True
            else:
                context['nodata']=False
        else:
            context['nodata']=False
            context['posts']=Post.objects.order_by('-date') 
    return render(request,'blogdisplay.html',context)
class PostDetails(DetailView):
    model=Post
    template_name='blogdetails.html'
    
def create(request):
    blogform=BlogForm()
    if request.method == 'POST':
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blogobj=blogform.save(commit=False)
            blogobj.author=request.user
            blogobj.save()
    data={}
    if blogform.errors:
        data['valid']=False
        for field in blogform.errors:
            # print(signupform.errors[field])
            data[f'{field}']=blogform.errors[field]
    else:
        data['valid']=True
    # print("data = " , data)
    return JsonResponse(data)