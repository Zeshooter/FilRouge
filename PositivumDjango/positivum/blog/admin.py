from django.contrib import admin
from .models import signature, type_evenement, evenement, commentaire, article, emotion, videotheque, oeuvre, professionnel, type_professionnel, type_oeuvre, categorie_oeuvre, citation, avatar

# Register your models here.
admin.site.register(signature)
admin.site.register(type_oeuvre)
admin.site.register(type_professionnel)
admin.site.register(type_evenement)
admin.site.register(emotion)
admin.site.register(evenement)
admin.site.register(commentaire)
admin.site.register(article)
admin.site.register(videotheque)
admin.site.register(oeuvre)
admin.site.register(professionnel)
admin.site.register(categorie_oeuvre)
admin.site.register(citation)
admin.site.register(avatar)