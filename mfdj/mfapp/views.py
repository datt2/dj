from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
# Create your views here.
#posts_ls=[{'author':'datt','age':'21'},{'author':'db2','age':'22'}]

def home(request):
    #context ={'posts':posts_ls}
    context = {'posts':Post.objects.all()}
    return render(request,'mfapp/home.html',context)

def about(request):
    return render(request,'mfapp/about.html')
