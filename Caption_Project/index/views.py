from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Image
from .models import Caption
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
        
    return redirect('success_upload')

#views for the caption page

def caption(request):
    images=list(Image.objects.all())
    rand_image=random.choice(images)
    context={
        'rand_image':rand_image
    }
    return render(request,'index/caption.html',context)


def success_upload(request):

    return render(request,'index/success_upload.html')

def success_caption_upload(request):
    if request.method== "POST":
        caption1=request.POST.get('caption1')
        caption2=request.POST.get('caption2')
        caption3=request.POST.get('caption3')
        caption4=request.POST.get('caption4')
        caption5=request.POST.get('caption5')
        ImageURL = request.POST.get('imageID')
     
        caption=Caption(caption1=caption1,caption2=caption2,caption3=caption3,caption4=caption4,caption5=caption5, imageURL=ImageURL)
        caption.save()

    return render(request,'index/success_caption_upload.html')
  
