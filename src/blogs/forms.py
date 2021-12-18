from django import forms
from django.core.files.images import get_image_dimensions
from django.forms.models import fields_for_model
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude=['author']
    def clean(self):
        # cost = self.cleaned_data['cost']
        # if (cost <= 0):
        #     self.add_error('cost','Cost must be positive and less than 100000!')
        image = self.cleaned_data['image']
        if(not image):
            self.add_error('image','Upload an Image!')
        else:
            w,h= get_image_dimensions(image)
            if(w<400 and h<300):
                self.add_error('image','Print image must be 400x300 wide')
            if(image.size>(1*1024*1024)):
                self.add_error('image','Print image must be less than 1MB')
        return super(BlogForm,self).clean()
