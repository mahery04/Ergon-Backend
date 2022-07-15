from django.db import models
from django.db.models.deletion import SET_DEFAULT
from employee.models import Personnel

# Create your models here.


class Depot(models.Model):
    Lieux = models.CharField(max_length=100)


class Materiel(models.Model):
    Designation = models.CharField(max_length=150)
    Emplacement = models.ForeignKey(
        'Depot', on_delete=models.PROTECT)
    Code = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    Quantite = models.IntegerField()
    # QuantiteEnService = models.IntegerField()
    # QuantiteDisponible = models.IntegerField()
    PrixDAchat = models.BigIntegerField()
    PrixDeLocation = models.BigIntegerField()
    PrixDeCasse = models.BigIntegerField()
    Consigne = models.CharField(max_length=255)

# >>>> Utilisateur à créer. Besoin de configuration.


class Entre_Sortie(models.Model):
    Date_Sortie = models.DateTimeField(auto_now=False, auto_now_add=False)
    Date_Retour = models.DateTimeField(auto_now=False, auto_now_add=False)
    # Employer à encore congigurer avec employé. Besoin de FK
    Magasinier = models.ForeignKey(
        Personnel, on_delete=models.PROTECT)
