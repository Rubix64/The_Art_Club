from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    artist=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,blank=False)
    time_created=models.DateTimeField(auto_now_add=True,blank=False)
    gallery_image=models.ImageField(upload_to='images/gallery/',blank=False)

    def __str__(self):
        return self.title+" ( By:"+self.artist.first_name+")"
    