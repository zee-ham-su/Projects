from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Fast'
    feature1.description = 'Our services is expedited'

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Reliable'
    feature2.description = 'Our services is very reliable'

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'Affordable'
    feature3.description = 'Our services is very affordable'

    return  render(request, 'index.html', {'feature': feature1, 'feature2': feature2, 'feature3': feature3})

def counter(request):
    text = request.POST['text']
    wordlist = len(text.split())
    return render(request, 'counter.html', {'words': wordlist})