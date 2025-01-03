from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
    # return HttpResponse("Hello World , You are at chai aur Django home page !!")
    return render(request,"website/index.html" )

def about(request):
    # return HttpResponse("Hello , World. You are at about Page.")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, World. You are at chai aur Django contact page")
    return render(request, 'website/contact.html')

def services(request):
    return render(request, 'website/services.html')
