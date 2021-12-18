from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=25)
    image= models.ImageField(upload_to='blogs/images/')
    # name=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    # author=models.CharField(max_length=30)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content=models.TextField()
    #published_date =datetime.strptime('04-12-2014', '%d-%m-%Y').date()
    # published_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    published_date =datetime.now().date()

    def __str__(self):
        return self.title+' : '+str(self.author)

    def get_absolute_url(self):
        #return reverse('PostDetails',args=str(self.id))
        return reverse('Blog')

