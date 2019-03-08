from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "BootGridApp/index.html")

def page2(request):
    return render(request, "BootGridApp/page2.html")

def page3(request):
    return render(request, "BootGridApp/page3.html")