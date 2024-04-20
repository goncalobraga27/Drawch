from django.urls import path 
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contacts",views.contacts,name="contacts"),
    path("paint",views.paint,name="paint"),
    path("paint.js",views.get_paint_js,name="get_paint.js"),
    path("paint.css",views.get_paint_css,name="get_paint.css"), 
    path("background.jpeg",views.get_background,name="get_background"),
    path("favicon.png",views.get_favicon,name="get_favicon"),
    path("home.png",views.get_home,name="get_home"),
    path("website.png",views.get_website,name="get_website"),
    path("about.png",views.get_about,name="get_about")
]