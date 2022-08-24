from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from .forms import FormulaireCommentaire
from .models import Commentaire, Oeuvre, Article, Emotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

# Create your views here.

def article_liste (request, oeuvrer=None):
    articles = Article.published.all()
    oeuvres = Oeuvre.objects.all()
    if oeuvrer:
        oeuvrer = get_object_or_404(Oeuvre, slug_oeuvre=oeuvrer)
        articles = articles.filter(oeuvrer=oeuvrer).order_by("publish")
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try :
        articles = paginator.page(page)
    except PageNotAnInteger :
        articles = paginator.page(1)
    except EmptyPage :
        articles = paginator.page(paginator.num_pages)
    context = {'articles':articles, 'page':page, 'oeuvres':oeuvres, 'oeuvrer':oeuvrer}
    return render(request, 'blog/articles/liste.html', context)

def article_detail(request, slug: str):
    article = get_object_or_404(Article, slug_article=slug)
    commentaire = Commentaire.objects.filter(commenter=article.id)
    nouveau_commentaire = None
    if request.method == 'POST':
        formulaire_commentaire = FormulaireCommentaire(data=request.POST)
        if formulaire_commentaire.is_valid():
            nouveau_commentaire = formulaire_commentaire.save(commit=False)
            nouveau_commentaire.commenter = article
            nouveau_commentaire.save()
    else:
        formulaire_commentaire = FormulaireCommentaire()
    return render(request, 'blog/articles/detail_article.html', {'article': article, 'commentaire':commentaire, 'nouveau_commentaire':nouveau_commentaire, "formulaire_commentaire":formulaire_commentaire})

# class ArticleListeVue(generic.ListView):
#     queryset = Article.objects.all()
#     paginate_by = 3
#     template_name = 'blog/articles/liste.html'
#     context_object_name = "articles"