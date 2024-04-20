from django.shortcuts import render, HttpResponse

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