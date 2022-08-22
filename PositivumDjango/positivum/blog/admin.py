from django.contrib import admin
from .models import Signature, Type_evenement, Evenement, Commentaire, Article, Emotion, Videotheque, Oeuvre, Professionnel, Type_professionnel, Type_oeuvre, Categorie_oeuvre, Citation, Avatar

# Register your models here.
admin.site.register(Signature)
admin.site.register(Type_oeuvre)
admin.site.register(Type_professionnel)
admin.site.register(Type_evenement)
admin.site.register(Emotion)
# admin.site.register(article)
admin.site.register(Evenement)
admin.site.register(Commentaire)
admin.site.register(Videotheque)
admin.site.register(Oeuvre)
admin.site.register(Professionnel)
admin.site.register(Categorie_oeuvre)
admin.site.register(Citation)
admin.site.register(Avatar)

@admin.register(Article)
class articleadmin(admin.ModelAdmin):
    list_display = ('titre_article','status_article','date_creation_article','publish','auteur')
    prepopulated_fields = {'slug_article':('titre_article',)}
    search_fields = ('titre_article', 'corps_article')
    ordering = ('auteur', 'status_article')
    list_filter = ('auteur', 'date_creation_article', 'publish')