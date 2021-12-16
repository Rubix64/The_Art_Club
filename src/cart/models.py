from django.db import models
from django.contrib.auth.models import User

from prints.models import Print

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    print=models.ForeignKey(Print,on_delete=models.CASCADE)
    qty=models.IntegerField(blank=False,default=1)
    time_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "print"),)

    def __str__(self):
        return self.user.username+" :- "+str(self.print.id)+"("+str(self.qty)+")"

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,blank=False)
    phno=models.IntegerField(blank=False)
    address=models.TextField(blank=False)
    city=models.CharField(max_length=50,blank=False)
    state=models.CharField(max_length=50,blank=False)
    zipcode=models.IntegerField(blank=False)
    time_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+"(Order id: "+str(self.id)+")"

class OrderItem(models.Model):
    DELIVERY_STATUS = (
        ('D', 'Delivered'),
        ('P', 'Pending'),
        ('C', 'Cancelled'),
    )
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    print=models.ForeignKey(Print, on_delete=models.CASCADE)
    qty=models.IntegerField(blank=False, default=1)
    status = models.CharField(max_length=1, choices=DELIVERY_STATUS, blank=False,default='P')

    class Meta:
        unique_together = (("order", "print"),)

    def __str__(self):
        return self.order.name+"(Order id:"+str(self.order.id)+":- "+str(self.print.id)+" qty:"+str(self.qty)+")"
    
    