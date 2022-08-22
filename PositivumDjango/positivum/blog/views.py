from django.shortcuts import render
from django.http import HttpResponse
from .models import Oeuvre, Article
# Create your views here.

def index(request):
    oeuvres = Oeuvre.objects.all()
    articles = Article.objects.all()
    print(articles)
    return render(request, 'blog/index.html', {"oeuvres": oeuvres, 'articles': articles})

def article_detail(request, slug: str):
    try:
        article = Article.objects.get(slug_article=slug)
        print(article)
    except Article.DoesNotExist:
        raise("Cet article n'existe pas")
    return render(request, 'blog/articles/detail_article.html', {'article': article})
