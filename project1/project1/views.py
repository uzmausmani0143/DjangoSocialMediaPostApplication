from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello Home!")
    return render (request, 'index.html')
   # return render (request, 'website/index.html')

def about(request):
    return HttpResponse("Hello About!")

def world(request):
    return HttpResponse("Hello World!")

