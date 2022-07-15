from django.db.models import fields
from rest_framework import serializers
from customer.models import Particulier, Rdv, Societe, Guest


class SocieteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Societe
        fields = ['Nom', 'Representant_Nom', 'Representant_Prenoms',
                  'Domiciliation', 'Contact', 'Email', 'NIF', 'STAT', 'RCS']


class ParticulierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particulier
        fields = ['Nom', 'Prenoms', 'Date_naissance',
                  'Lieu_naissance', 'CIN', 'CIN_date_delivrance', 'CIN_recto', 'CIN_verso', 'Certificat_residence', 'Lieu_residence', 'Contact1', 'Contact2', 'Email']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['Nom', 'Prenoms', 'Contact']


class RdvSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Rdv
        fields = ['Customer', 'Date_Darrivé',
                  'Date_Depart', 'Disponibilite', 'Motif', 'Etat']
