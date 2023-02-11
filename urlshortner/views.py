from django.shortcuts import render,redirect

import random
from .models import Url
import string
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def createshorturl(request):
    if (request.method == 'POST' and request.POST["url"]):
        
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = request.POST["url"]
            new_url = Url(url=url, slug=slug)
            new_url.save()
         
            messages.info(request,'New URL is created you can check it on view urls')
            return redirect('/')
    else:
       messages.info(request,'Please enter a valid url')
       return redirect('/')
  
def urlcreated(request):
    url=Url.objects.all()
    urlObject = request.get_host()+ '/'
    return render(request,'urls.html',{'url':url, 'homeurl': urlObject})

def findredirect(request, slg):
    url=Url.objects.get(slug= slg)
    return redirect(url.url)
