from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class Type_professionnel(models.Model):
    nom_type_professionnel = models.CharField(max_length=50)
    explication_metier_professionnel = models.TextField(blank=True)

    def __str__(self):
        return self.nom_type_professionnel

class Professionnel(models.Model):
    prenom_professionnel = models.CharField(max_length=50, blank=True)
    nom_professionnel = models.CharField(max_length=50)
    date_naissance_professionnel = models.DateField(null=True, blank=True)
    resume_carriere_professionnel = models.TextField(blank=True)
    photo_professionnel = models.ImageField(upload_to='photo_pro', blank=True)
    type_professionnel = models.ForeignKey(Type_professionnel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_professionnel

# ex : Film, série, salle etc
class Type_oeuvre(models.Model):
    nom_type_oeuvre = models.CharField(blank=False,max_length=50)

    def __str__(self):
        return self.nom_type_oeuvre

# ex : Comédie, sf, Action, Film d'auteur etc
class Categorie_oeuvre(models.Model):
    nom_categorie_oeuvre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.nom_categorie_oeuvre

# ex : citation de passage de l'oeuvre (répliques de films)
class Citation(models.Model):
    text_citation = models.TextField(blank=True)

    def __str__(self):
        return self.text_citation

class Oeuvre(models.Model):
    nom_oeuvre = models.CharField(max_length=100)
    synopsis_oeuvre = models.TextField(blank=True)
    visuel_oeuvre = models.ImageField(upload_to='visuel_oeuvre', blank=True)
    video_oeuvre = models.FileField(upload_to='videos_oeuvre', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    categorie_oeuvre = models.ForeignKey(Categorie_oeuvre, on_delete=models.CASCADE)
    type_oeuvre = models.ForeignKey(Type_oeuvre, on_delete=models.CASCADE)
    professionnel = models.ManyToManyField(Professionnel, blank=True)

    def __str__(self):
        return self.nom_oeuvre


class Emotion(models.Model):
    nom_emotion = models.CharField(max_length=50)
    visuel_emotion = models.ImageField(upload_to="emotion", blank=True)
    definition_emotion = models.TextField(blank=True)

    def __str__(self):
        return self.nom_emotion

class Article(models.Model):
    STATUS_CHOICES = (
        ('brouillon', 'Brouillon'),
        ('publié', 'Publié'),
    )
    titre_article = models.CharField(max_length=200)
    slug_article = models.SlugField(max_length=200, null=True)
    visuel_article = models.ImageField(upload_to="visuel_article", blank=True, null=True)
    corps_article = models.TextField(blank=True)
    date_creation_article = models.DateTimeField(auto_now_add=True, null=True)
    date_maj_article = models.DateTimeField(auto_now=True, null=True)
    status_article = models.CharField(choices=STATUS_CHOICES, default='brouillon', max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    citer = models.ManyToManyField(Citation, blank=True)
    ressentir = models.ManyToManyField(Emotion, blank=True)
    oeuvrer = models.ManyToManyField(Oeuvre)

    def __str__(self):
        return self.titre_article

class Commentaire(models.Model):
    date_heure_commentaire = models.DateTimeField( default=datetime.now, null=True)
    titre_commentaire = models.CharField(max_length=50)
    corps_commentaire = models.TextField(blank=True)
    commenter = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_commentaire

class Type_evenement(models.Model):
    nom_type_evenement = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_type_evenement

class Evenement(models.Model):
    titre_evenement = models.CharField(max_length=100)
    visuel_evenement = models.ImageField(upload_to="visuel_evenement", null=True)
    description_evenement = models.TextField(blank=True)
    date_heure_evenement = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    lieu_evenement = models.CharField(max_length=100)
    type_evenement = models.ForeignKey(Type_evenement, on_delete=models.CASCADE)
    organiser = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.titre_evenement

class Signature(models.Model):
    texte_signature = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.texte_signature

class Videotheque(models.Model):
    nom_videotheque = models.CharField(max_length=100)
    voir = models.ManyToManyField(Oeuvre)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_videotheque

class Avatar(models.Model):
    visuel_avatar = models.ImageField(upload_to="visuel_avatar")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.visuel_avatar






