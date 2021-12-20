from django import forms
from django.core.files.images import get_image_dimensions
from django.forms.models import fields_for_model
from .models import *

class PrintForm(forms.ModelForm):
    class Meta:
        model= Print
        exclude=['artist']
    # description = forms.CharField(widget=forms.Textarea)
    def clean(self):
        cost = self.cleaned_data['cost']
        if (cost <= 0):
            self.add_error('cost','Cost must be positive and less than 100000!')
        print_image = self.cleaned_data['print_image']
        if(not print_image):
            self.add_error('print_image','Upload an Image!')
        else:
            w,h= get_image_dimensions(print_image)
            if(w<400 and h<300):
                self.add_error('print_image','Print image must be 400x300 wide')
            if(print_image.size>(1*1024*1024)):
                self.add_error('print_image','Print image must be less than 1MB')
        return super(PrintForm,self).clean()
