from django import forms
from django.core.files.images import get_image_dimensions
from django.forms.models import fields_for_model
from .models import *

class GalleryForm(forms.ModelForm):
    class Meta:
        model= Gallery
        exclude=['artist']
    def clean(self):
        gallery_image = self.cleaned_data['gallery_image']
        if(not gallery_image):
            self.add_error('gallery_image','Upload an Image!')
        else:
            w,h= get_image_dimensions(gallery_image)
            if(w<400 and h<300):
                self.add_error('gallery_image','Print image must be 400x300 wide')
            if(gallery_image.size>(1*1024*1024)):
                self.add_error('gallery_image','Print image must be less than 1MB')
        return super(GalleryForm,self).clean()
