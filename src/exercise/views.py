from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
	template = loader.get_template('exercise/index.html')
	context = {}
	return render(request, 'exercise/index.html', context)

def home(request):
    context = {}
    return render(request, 'home.html', context)
def contactus(request):
    context = {}
    return render(request, 'contactus.html', context)
def coursecontents(request):
	context = {}
	return render(request, 'coursecontents.html', context)
