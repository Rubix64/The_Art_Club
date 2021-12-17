from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from .models import *
from .forms import *

from cart.views import no_of_contents

# Create your views here.
def prints(request):
    context={}
    context['no_of_contents']= no_of_contents(request.user)
    # print(context['no_of_contents'])
    if(Print.objects.count() == 0):
        context['nodata']=True 
    else:
        if request.method == 'GET' and request.GET.get('artistsearch'):
            artistsearch = request.GET.get('artistsearch')
            context['prints']=Print.objects.filter(artist__first_name__icontains=artistsearch).order_by('-time_created')
            if(context['prints'].count() == 0):
                context['nodata']=True
            else:
                context['nodata']=False
        else:
            context['nodata']=False
            context['prints']=Print.objects.order_by('-time_created') 
    return render(request,'prints.html',context)

def printdata(request):
    printform=PrintForm()
    if request.method == 'POST':
        printform = PrintForm(request.POST, request.FILES)
        if printform.is_valid():
            printobj=printform.save(commit=False)
            printobj.artist=request.user
            printobj.save()
    data={}
    if printform.errors:
        data['valid']=False
        for field in printform.errors:
            # print(signupform.errors[field])
            data[f'{field}']=printform.errors[field]
    else:
        data['valid']=True
    # print("data = " , data)
    return JsonResponse(data)