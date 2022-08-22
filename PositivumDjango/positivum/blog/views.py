from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Oeuvre, Article

# Create your views here.

def index(request):
    oeuvres = Oeuvre.objects.all()
    articles = Article.objects.all()
    print(articles)
    return render(request, 'blog/index.html', {"oeuvres": oeuvres, 'articles': articles})

def article_detail(request, slug: str):
    article = get_object_or_404(Article, slug_article=slug)
    return render(request, 'blog/articles/detail_article.html', {'article': article})
