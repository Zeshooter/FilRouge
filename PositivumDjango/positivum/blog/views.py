from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Oeuvre, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

# Create your views here.

def article_liste (request):
    oeuvres = Oeuvre.objects.all()
    # object_list = Article.objects.all()
    # paginator = Paginator(object_list, 3)
    # page = request.GET.get('page')
    # try :
    #     articles = paginator.page(page)
    # except PageNotAnInteger :
    #     articles = paginator.page(1)
    # except EmptyPage :
    #     articles = paginator.page(paginator.num_pages)
    # context = {'articles':articles, 'page':page, 'oeuvres':oeuvres}
    return render(request, 'blog/articles/liste.html', {'oeuvres':oeuvres})

def article_detail(request, slug: str):
    article = get_object_or_404(Article, slug_article=slug)
    return render(request, 'blog/articles/detail_article.html', {'article': article})

class ArticleListeVue(generic.ListView):
    queryset = Article.objects.all()
    paginate_by = 3
    template_name = 'blog/articles/liste.html'
    context_object_name = "articles"