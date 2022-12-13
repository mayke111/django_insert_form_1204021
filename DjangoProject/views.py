from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from . import forms


def index(request):

    db = Post.objects.all()
    context = {
        'title':'picah',
        'post': db
    }
    return render (request,'index.html', context);

def form(request):
    classform =  forms.pukulpedo()

    context = {
        'title': 'sb',
        'classform': classform
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['alamat'] = request.POST['alamat']
        context['namac'] = request.POST['namac']
        context['alamatc'] = request.POST['alamatc']
    else:
        # return render(request, 'form.html')
        print("ini get")
    return render(request, 'form.html', context,)
    

def articles(request,year):
    year=year 
    str=year
    return HttpResponse(year)