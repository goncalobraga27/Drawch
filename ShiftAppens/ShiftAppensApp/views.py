from django.shortcuts import render, HttpResponse
import os
from django.http import FileResponse, HttpResponseNotFound
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


def contacts(request):
    return render(request,"contacts.html")

def paint(request):
    return render(request,"paint.html")

def get_paint_js(request):
    return render(request,"paint.js")

def get_paint_css(request):
    return render(request,"paint.css")

def get_background(request):
    background_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "background.jpeg")
    if os.path.exists(background_path):
        return FileResponse(open(background_path, 'rb'), content_type='image/jpeg')
    else:
        return HttpResponseNotFound()
    
def get_favicon(request):
    background_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.png")
    if os.path.exists(background_path):
        return FileResponse(open(background_path, 'rb'), content_type='image/png')
    else:
        return HttpResponseNotFound()
    
def get_home(request):
    background_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "home.png")
    if os.path.exists(background_path):
        return FileResponse(open(background_path, 'rb'), content_type='image/png')
    else:
        return HttpResponseNotFound()

def get_website(request):
    background_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "website.png")
    if os.path.exists(background_path):
        return FileResponse(open(background_path, 'rb'), content_type='image/png')
    else:
        return HttpResponseNotFound()

def get_about(request):
    background_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "about.png")
    if os.path.exists(background_path):
        return FileResponse(open(background_path, 'rb'), content_type='image/png')
    else:
        return HttpResponseNotFound()