from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render_to_response, render

# Create your views here.
def index(request):
        return render(request, 'index.html', {'nbar': 'home'})

def about(request):
        return render(request, 'index.html', {'nbar': 'about'})

def causes(request):
        return render(request, 'causes.html', {'nbar': 'causes'})

def gallery(request):
        return render(request, 'portfolio.html', {'nbar': 'gallery'})

def news(request):
        return render(request, 'news.html', {'nbar': 'news'})

def contact(request):
        return render(request, 'contact.html', {'nbar': 'contact'})