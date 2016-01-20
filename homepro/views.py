from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout

# Create your views here.
def home(request):
	page = "initial.html"
	context = {}
	return render(request,page,context)

def logout(request):
    auth_logout(request)
    return redirect('/')