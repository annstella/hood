from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile, Business, NeighbourHood
from .forms import BusinessForm
import datetime as dt
from django.contrib import messages
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# from .forms import NewsLetterForm

# Create your views here.
@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def business(request):
	'''
	View function that returns all added user businesses
	'''
	businesses= Business.objects.filter(user = request.user)
	return render(request,'business.html',locals())


@login_required(login_url='/accounts/login/')
def new_business(request):
	'''
	View function that enables users to add businesses
	'''
	if request.method == 'POST':
		form = BusinessForm(request.POST)
		if form.is_valid():
			business = form.save(commit = False)
			business.user = request.user
			business.save()
			messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
			return redirect('business')

	else:
		form = BusinessForm()
		return render(request,'new_business.html',locals())


@login_required(login_url='/accounts/login/')
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