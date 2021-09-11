from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Image
import random

def home(request):
    return render(request,'index/home.html')



def register(request):
    if request.method=='POST':
         form=UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request,f'Hi {username},your account was created successfully')
             return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'index/register.html',{'form':form})


def login(request):
    return render(request,'index/login.html')


def index(request):
    return render(request,'index/index.html')

def logout(request):
    return render(request,'index/login.html')


def upload(request):
    return render(request,'index/upload.html')

def upload_save(request):
    images=request.FILES.getlist("file[]")
    for img in images:
        fs=FileSystemStorage()
        file_path=fs.save(img.name,img)
        images=Image(image=file_path)
        images.save()
        
     return redirect('caption')

#views for the caption page

def caption(request):
    images=list(Image.objects.all())
    rand_image=random.choice(images)
    context={
        'rand_image':rand_image
    }
    return render(request,'index/caption.html',context)
