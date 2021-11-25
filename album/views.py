from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ModeForm

# Create your views here.
from album.models import collection


def home(request):
    items=collection.objects.all()
    return render(request,"main.html",{'items':items})

def add(request):
    if request.method=="POST":
        img = request.FILES['img']
        desc=request.POST['desc']
        s=collection(image=img,name=desc)
        s.save()
        return redirect('home')
    return render(request,"add.html")

def update(request,id):
    obj=collection.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,"update.html",{'form':form,'obj':obj})


def delete(request,id):
    if request.method=='POST':
        obj=collection.objects.get(id=id)
        obj.delete()
        return redirect('home')
    return render(request,"delete.html")