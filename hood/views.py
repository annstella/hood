from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile, Business, NeighbourHood
import datetime as dt

# Create your views here.
def welcome(request):
    # hood = Business.objects.all() 
    return render(request,'index.html', locals())


def search_results(request):

    if 'Business' in request.GET and request.GET["Business"]:
        search_term = request.GET.get("Business")
        searched_Business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-hood/search.html',{"message":message,"Business": searched_Business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-hood/search.html',{"message":message})