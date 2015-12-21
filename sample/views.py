from django.shortcuts import render
from .forms import SignUpModelForm, ContactForm
# Create your views here.
def home(request):
	title = "Welcome"
	if request.user.is_authenticated():
		title = "My Title %s" %(request.user)
		form = SignUpModelForm(request.POST)

	context = {
		"template_title": title,
		"form" : form
	}

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Dummy"
		instance.save()
		context = {
			"title":"Thank You"
		}
	
	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
			
	context = {
		"form" : form,
	}

	return render(request,"forms.html",context)