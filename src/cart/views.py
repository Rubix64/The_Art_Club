from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Sum
import json

from .models import *
from prints.models import *

# Create your views here.
def no_of_contents(user):
    if user.is_authenticated:
        totalqty=Cart.objects.filter(user=user).aggregate(Sum('qty'))
        if totalqty['qty__sum']==None:
            return 0
        else:
            return totalqty['qty__sum']
    else:
        return 0

def cart(request):
    context={}
    context['no_of_contents']= no_of_contents(request.user)
    if request.user.is_authenticated:
        if Cart.objects.filter(user=request.user).count()==0:
            context['nodata']=True
        else:
            context['nodata']=False
            cart_items=Cart.objects.filter(user=request.user).order_by('-time_created')
            context['cart_items']=cart_items
            cost=0
            for cart_item in cart_items:
                cost+=cart_item.qty*cart_item.print.cost
            context['totcost']=cost
    return render(request, 'cart.html',context)

def cartadd(request):
    data={}
    if not request.user.is_authenticated:
        data['loggedin']=False
        return JsonResponse(data)
    data['loggedin'] = True
    if request.user and request.is_ajax and request.method == 'GET':
        # print(request.GET.get('printid'))
        printid=int(request.GET.get('printid'))
        if Print.objects.filter(id=printid).exists():
            printobj=Print.objects.filter(id=printid)[0]
            content=Cart.objects.filter(user=request.user,print=printobj).first()
            if content is None:
                Cart.objects.create(user=request.user,print=printobj,qty=1)
            else:
                qt=content.qty
                qt=qt+1
                # print(content)
                Cart.objects.filter(user=request.user,print=printobj).update(qty=qt)
            data['success']=True
            data['totalqty']=no_of_contents(request.user)
        else:
            data['success']=False
    else:
        data['success']=False
    return JsonResponse(data)


        
            
