from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import *
from django.views.generic import ListView

def gallery(request):
    return render(request,'gallery.html')

def galleries(request):
    context={}
    if(Gallery.objects.count() == 0):
        context['nodata']=True 
    else:
        context['nodata']=False
        context['galleries']=Gallery.objects.order_by('-time_created') 
    return render(request,'gallery.html',context)

def gallerydata(request):
    print("woooo");
    print(request.FILES)
    galleryform=GalleryForm()
    if request.method == 'POST':
        galleryform = GalleryForm(request.POST, request.FILES)
        if galleryform.is_valid():
            galleryobj=galleryform.save(commit=False)
            galleryobj.artist=request.user
            galleryobj.save()

    data={}
    if galleryform.errors:
        data['valid']=False
        for field in galleryform.errors:
            # print(signupform.errors[field])
            data[f'{field}']=galleryform.errors[field]
    else:
        data['valid']=True
    # print("data = " , data)
    return JsonResponse(data)

# class galleryimages(ListView):
#     model=Gallery
#     template_name="gallery.html"

# def uploaded_image(request):
#     img=Gallery.objects.all()
#     context={
#         'uploaded_image': img
#     }
#     return render(request, 'gallery.html',context)