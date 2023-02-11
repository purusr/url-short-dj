from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('createshorturl',views.createshorturl,name="createshorturl"),
    path("urlcreated",views.urlcreated,name="urlcreated"), 
    path("<str:slg>",views.findredirect,name="urlcreated"), 
]