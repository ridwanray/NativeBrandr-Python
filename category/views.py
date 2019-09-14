from user.models import Design
from django.shortcuts import render	
	
def cap(request):
	tests = Design.objects.filter(category__name="cap")
	return render(request, 'categorypage.html', {"tests":tests})	
def trousersshirts(request):
	tests = Design.objects.filter(category__name="trousers&shirts")
	return render(request, 'categorypage.html', {"tests":tests})
def customizedvest(request):
	tests = Design.objects.filter(category__name="customized-vest")
	return render(request, 'categorypage.html', {"tests":tests})
def bagsaddons(request):
	tests = Design.objects.filter(category__name="bags&add-ons")
	return render(request, 'categorypage.html', {"tests":tests})
def jewelry(request):
	tests = Design.objects.filter(category__name="jewelry")
	return render(request, 'categorypage.html', {"tests":tests})
def nativewears(request):
	tests = Design.objects.filter(category__name="native-wears")
	return render(request, 'categorypage.html', {"tests":tests})
def shirts(request):
	tests = Design.objects.filter(category__name="shirts")
	return render(request, 'categorypage.html', {"tests":tests})
def footwears(request):
	tests = Design.objects.filter(category__name="footwears")
	return render(request, 'categorypage.html', {"tests":tests})