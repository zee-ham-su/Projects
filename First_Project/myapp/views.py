from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return  render(request, 'index.html')

def counter(request):
    words = request.GET['text']
    wordlist = words.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    return render(request, 'counter.html', {'words':words, 'count':len(wordlist), 'worddictionary':worddictionary.items()})