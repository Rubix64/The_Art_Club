from django import forms
import re

from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        exclude=['user']

    def clean(self):
        phno = self.cleaned_data['phno']
        zipcode=self.cleaned_data['zipcode']
        if (len(str(phno))!=10 and not re.search("^[0-9]{10}$",phno)):
            self.add_error('phno','Enter a valid phone number.')
        elif(len(str(zipcode))!=6 and not re.search("^[0-9]{10}$",zipcode)):
            self.add_error('zipcode','Enter a valid zipcode.')
        return super(OrderForm,self).clean()
