from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LnadingPageEntryModelForm
from .models import LnadingPageEntry

def home_page(request,*args,**kwargs):
    title= "Welcome home"
    form=LnadingPageEntryModelForm(request.POST or None)

    name=request.POST.get('name')
    email=request.POST.get('email')
    if form.is_valid():
        obj=form.save()
        print(obj)

        #another methods to store data
        #print(form.cleaned_data)
        #name=form.cleaned_data.get('name')
        #email=form.cleaned_data.get('email')
        #obj=LnadingPageEntry.objects.create(name=name,email=email)
        #obj.save()
        form=LnadingPageEntryModelForm()
        
    print(name,email)
    context={"title":title,
             "form":form}
    return render(request,"landing_pages/home.html",context)
