from django.db import models


class Client(models.Model):
    CAT_CLIENT = [
        ('PAR', 'Particulier'),
        ('SOC', 'Societe'),
        ('GUE', 'Guest')
    ]
    categorie_client = models.CharField(
        max_length=3, choices=CAT_CLIENT, default="GUE")


class Societe(models.Model):
    Nom = models.CharField(max_length=120)
    Representant_Nom = models.CharField(max_length=120)
    Representant_Prenoms = models.CharField(max_length=120)
    Domiciliation = models.CharField(max_length=300)
    Contact = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    # Configuration à faire (storage, path...)
    NIF = models.ImageField(upload_to='Societe/')
    # Configuration à faire (storage, path...)
    STAT = models.ImageField(upload_to='Societe/')
    # Configuration à faire (storage, path...)
    RCS = models.ImageField(upload_to='Societe/')
    Customer = models.ForeignKey(
        'Client', on_delete=models.CASCADE, default='None')


class Particulier(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    Lieu_naissance = models.CharField(max_length=300)
    CIN = models.BigIntegerField(null=False)
    CIN_date_delivrance = models.DateField(auto_now=False, auto_now_add=False)
    # Configuration à faire (storage, path...)
    CIN_recto = models.ImageField(upload_to='Particulier/')
    # Configuration à faire (storage, path...)
    CIN_verso = models.ImageField(upload_to='Particulier/')
    # Configuration à faire (storage, path...)
    Certificat_residence = models.ImageField(upload_to='Particulier/')
    Lieu_residence = models.CharField(max_length=300)
    Contact1 = models.CharField(max_length=10)
    Contact2 = models.CharField(max_length=10)
    Email = models.EmailField(max_length=255)
    Customer = models.ForeignKey(
        'Client', on_delete=models.CASCADE, default='None')


class Guest(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Contact = models.CharField(max_length=10)


class Rdv(models.Model):
    # Toutes les entités qui prennent des rdv seront considéré comme des guests.
    # Les opérations à effectuer sont à indiquer dessus.

    CHOIX_ETAT = [
        ('ANN', 'Annuler'),
        ('REP', 'Reporter'),
        ('ACT', 'Actif')
    ]

    MOTIF = [
        ('VIS', 'Visite'),
        ('REN', 'Renseignement'),
        ('CON', 'Signature de Contrat'),
        ('PAI', 'Paiement')
    ]

    Customer = models.ForeignKey(
        'Guest', on_delete=models.CASCADE, default='None')
    Date_RDV = models.DateTimeField(auto_now=False, auto_now_add=False)
    Motif = models.CharField(max_length=3, choices=MOTIF, default="VIS")
    Etat = models.CharField(max_length=3, choices=CHOIX_ETAT, default="ACT")
