from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, 'home.html', context)
def contactus(request):
    context = {}
    return render(request, 'contactus.html', context)
def coursecontents(request):
	context = {}
	return render(request, 'coursecontents.html', context)

def exercise(request):
	context = {}
	return render(request, 'exerciseIndex.html', context)
