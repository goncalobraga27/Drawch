from django.urls import path 
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contacts",views.contacts,name="contacts"),
    path("paint",views.paint,name="paint"),
    path("paint.js",views.get_paint_js,name="get_paint.js"),
    path("paint.css",views.get_paint_css,name="get_paint.css")
]