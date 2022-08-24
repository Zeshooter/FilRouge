
from django import forms

from .models import Commentaire

class FormulaireCommentaire (forms.ModelForm):
    titre_commentaire = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    corps_commentaire = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    class Meta:
        model = Commentaire
        fields = ['titre_commentaire', 'corps_commentaire']