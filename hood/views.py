from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile, Business, NeighbourHood
import datetime as dt
from .email import send_welcome_email
from .forms import NewsLetterForm

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

def business(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Business"
    businesses = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'business.html',{'title':title,"businesses":businesses})

# def new_business(request):
#     current_user = request.user
#     businesses=Business.objects.get(user=request.user)
#     hood= Business.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = BusinessForm(request.POST, request.FILES,instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#         return redirect('/')

#     else:
#         form = BusinessForm()
#     return render(request, "new_business.html", {"form":form}) 

def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Profile"
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile/profile.html',{'title':title,"profiles":profiles})

def hood(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('hood')
            #.................
    return render(request, 'index.html', {"hood":hood,"letterForm":form})