from django.shortcuts import render, redirect
from .models import photo
from .forms import ModeForm
# Create your views here.
def index(request):
    obj=photo.objects.all()
    return  render(request,'index.html',{'results':obj})


def details(request,photo_id):
    t=photo.objects.get(id=photo_id)
    return render(request,'details.html',{'p':t})


def update(request,id):
    obj=photo.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})


def delete(request,id):
    if request.method == 'POST':
         obj=photo.objects.get(id=id)
         obj.delete()
         return redirect('/')
    return render(request,'delete.html')


def about(request):
    return  render(request,'about.html')

def concerts(request):
    return  render(request,'concerts.html')
def contacts(request):
    return render(request,'contact.html')


