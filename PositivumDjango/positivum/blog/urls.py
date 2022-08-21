from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/liste/', views.liste_article, name='liste_articles'),
]
