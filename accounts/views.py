from django.shortcuts import render,redirect
from accounts.forms import UserAdminCreationForm
# Create your views here.


def Home(request):
	return render(request,"index.html")

def register(request):
	form=UserAdminCreationForm()
	if request.method=='POST':
		form=UserAdminCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	return render(request,"registration/register.html")

def product_view(request):
	return render(request,"product.html")	