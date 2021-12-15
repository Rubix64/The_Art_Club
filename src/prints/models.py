from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Print(models.Model):
    artist=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,blank=False)
    description=models.TextField(blank=False)
    cost=models.DecimalField(max_digits=7,decimal_places=2,blank=False)
    time_created=models.DateTimeField(auto_now_add=True,blank=False)
    print_image=models.ImageField(upload_to='prints/images',blank=False)

    def __str__(self):
        return self.title+" ( By:"+self.artist.first_name+")"+" -Rs."+str(self.cost)
    