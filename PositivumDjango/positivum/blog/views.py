from django.shortcuts import render
from django.http import HttpResponse
from .models import oeuvre, article
# Create your views here.

def index(request):
    oeuvres = oeuvre.objects.all()
    return render(request, 'blog/index.html', {"oeuvres":oeuvres})

def liste_article(request):
    articles = article.objects.all()
    return render(request,'blog/index.html',{'articles': articles})