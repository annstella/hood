from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    hood = Business.objects.all() 
    return render(request,'index.html', locals())
