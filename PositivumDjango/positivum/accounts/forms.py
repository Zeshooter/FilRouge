from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=250, min_length=5, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "username", "type": "text", "placeholder": "Username", "data-sb-validations": "required"}))

    prenom = forms.CharField(label="prenom", max_length=250, min_length=3, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "prenom", "type": "text", "placeholder": "Prénom", "data-sb-validations": "required"}))

    nom = forms.CharField(label="nom", max_length=250, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "nom", "type": "text", "placeholder": "Nom", "data-sb-validations": "required"}))

    email = forms.EmailField(label="emailAdress", max_length=250, min_length=5, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "email", "type": "email", "placeholder": "Adresse Email", "data-sb-validations": "required"}))

    password = forms.CharField(label="password", max_length=250, min_length=8, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "password", "type": "password", "placeholder": "Mot de passe", "data-sb-validations": "required"}))

    confirmation_mot_de_passe = forms.CharField(label="confirmationMotDePasse", max_length=250, min_length=8, help_text='', required=True, widget=forms.TextInput(
        attrs={"class": "form-control", "id": "confirmation_mot_de_passe", "type": "password", "placeholder": "Confirmer votre mot de passe", "data-sb-validations": "required"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
