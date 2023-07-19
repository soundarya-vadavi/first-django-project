from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList
from .models import LnadingPageEntry


class LnadingPageEntryModelForm(forms.ModelForm):
    name= forms.CharField(required=False)
    email2=forms.EmailField(label="Confirm Email")

    class Meta:
        model=LnadingPageEntry
        fields=["name","email"]
    
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            
            default_css_class='form-control'
            new_attrs={"class":default_css_class,
                       "id":f"{field}",
                       "placeholder":f"your { field}",}
                
            if field == "email2":
                new_attrs['placeholder']=f"Confirm your email"
            print('------------------')
            print(self.fields)
            self.fields[field].widget.attrs.update(new_attrs)
            print('-- --- --- --- -- ')
            print(self.fields)
            print('-- --- --- --- -- ')
    
    
    def clean(self):
        data=self.cleaned_data
        email1=data.get('email')
        email2=data.get('email2')
        if email2 != email1:
            self.add_error('email2','Your email must match!')
        return data                                                                                                      

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email.endswith('gmail.com'):
            self.add_error('email','You cannot use gmail')
        return email
                                                                                                                




class LnadingPageForm(forms.Form):
    
    name= forms.CharField(required=False)
    email=forms.EmailField()
    email2=forms.EmailField(label="Confirm Email")
    
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            
            default_css_class='form-control'
            new_attrs={"class":default_css_class,
                       "id":f"{field}",
                       "placeholder":f"your { field}",}
                
            if field == "email2":
                new_attrs['placeholder']=f"Confirm your email"
            print('------------------')
            print(self.fields)
            self.fields[field].widget.attrs.update(new_attrs)
            print('-- --- --- --- -- ')
            print(self.fields)
            print('-- --- --- --- -- ')
    


            
            
            


    def clean(self):
        data=self.cleaned_data
        email1=data.get('email')
        email2=data.get('email2')
        if email2 != email1:
            self.add_error('email2','Your email must match!')
        return data                                                                                                      

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email.endswith('gmail.com'):
            self.add_error('email','You cannot use gmail')
        return email
