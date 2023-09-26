from django.shortcuts import render

# Create your views here.

product=[{"name":'apple','status':'available'},{'name':'orange','status':'not available'},{'name':'banana','status':'not available'}]

def home(request):
    return render(request,"home.html",{"product":product})

def index(request):
    return render(request,"index.html")