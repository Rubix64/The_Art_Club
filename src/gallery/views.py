from django.shortcuts import render
from .models import Gallery
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


# class galleryimages(ListView):
#     model=Gallery
#     template_name="gallery.html"

# def uploaded_image(request):
#     img=Gallery.objects.all()
#     context={
#         'uploaded_image': img
#     }
#     return render(request, 'gallery.html',context)