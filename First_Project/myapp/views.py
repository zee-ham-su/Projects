from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Fast'
    feature1.description = 'Our application is fast'
    return  render(request, 'index.html', {'feature': feature1})

def counter(request):
    text = request.POST['text']
    wordlist = len(text.split())
    return render(request, 'counter.html', {'words': wordlist})