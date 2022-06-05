from django.shortcuts import render
import requests
API_KEY='3b39469e194c4d3ebc071e858ca902d3'
# Create your views here.

def index(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data=requests.get(url)
    response=data.json() 
    articles=response['articles']
    context={'articles': articles}
    return render(request, 'index.html',context)

def search(request):
    if request.method == 'POST':
        search_term = request.POST['search']
        url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey=3b39469e194c4d3ebc071e858ca902d3'
        data = requests.get(url)
        response = data.json()
        articles = response['articles']
        context = {'articles':articles,'search':search_term}
        return render(request,'search.html',context)

def business(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'business.html',context)
def entertainment(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'entertainment.html',context)

def health(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'health.html',context)   
def Science(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=Science&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'Science.html',context)   
def sports(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'sports.html',context) 
def technology(request):
    url=' https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3b39469e194c4d3ebc071e858ca902d3'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'technology.html',context)     