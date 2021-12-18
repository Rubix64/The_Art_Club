from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import *
from django.views.generic import ListView

from cart.views import no_of_contents

# def gallery(request):
#     return render(request,'gallery.html')

def galleries(request):
    context={}
    context['no_of_contents']= no_of_contents(request.user) 
    if(Gallery.objects.count() == 0):
        context['nodata']=True 
    else:
        if request.method == 'GET' and request.GET.get('artistsearch'):
            artistsearch = request.GET.get('artistsearch')
            context['galleries']=Gallery.objects.filter(artist__first_name__icontains=artistsearch).order_by('-time_created') 
            if(context['galleries'].count() == 0):
                context['nodata']=True
            else:
                context['nodata']=False
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