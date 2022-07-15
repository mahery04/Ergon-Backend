from django.db import models
from django.db.models.deletion import PROTECT

# On aurait besoin de mettre une catégorie de personnel (magasinier, mantention, intendant...)


class Personnel(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    Lieu_naissance = models.CharField(max_length=300)
    CIN = models.BigIntegerField()
    CIN_date_delivrance = models.DateField(auto_now=False, auto_now_add=False)
    # Configuration à faire (storage, path...)
    CIN_recto = models.ImageField(upload_to='Personnel/')
    # Configuration à faire (storage, path...)
    CIN_verso = models.ImageField(upload_to='Personnel/')
    # Configuration à faire (storage, path...)
    Certificat_residence = models.ImageField(upload_to='Personnel/')
    Lieu_residence = models.CharField(max_length=300)
    Contact1 = models.CharField(max_length=10)
    Contact2 = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)


class Congee(models.Model):
    Salarie = models.ForeignKey(
        'Personnel', on_delete=models.CASCADE, default='None')
    jour_congé = models.IntegerField()
    date_congé = models.DateField(auto_now=False)


class Historique(models.Model):
    Salarie = models.ForeignKey(
        'Personnel', on_delete=models.CASCADE, default='None')
    date_recrutement = models.DateTimeField(auto_now=False)
    date_demission = models.DateField(auto_now=False)


class Salaire(models.Model):
    Salarie = models.ForeignKey(
        'Personnel', on_delete=models.CASCADE, default='None')
    salaire = models.IntegerField()
    avance = models.IntegerField()
