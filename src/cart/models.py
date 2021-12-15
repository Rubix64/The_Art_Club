from django.db import models
from django.contrib.auth.models import User

from prints.models import Print

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    print=models.ForeignKey(Print,on_delete=models.CASCADE)
    qty=models.IntegerField(blank=False,default=1)
    time_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username+" :- "+str(self.print.id)+"("+str(self.qty)+")"