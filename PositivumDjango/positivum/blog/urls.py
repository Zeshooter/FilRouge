from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path ('', views.article_liste, name='index'),
    # path ('liste.html', views.article_liste, name='liste'),
    path ('<slug>/', views.article_detail, name='article_detail'),
    path('', views.ArticleListeVue.as_view(), name='article_liste'),
]
