from rest_framework import serializers
from titan.models import Bon_Livraison_Titan, Commande_Titan


class Commande_TitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande_Titan
        fields = ['client', 'date_Reservation',
                  'date_Sortie_Matériel', 'date_Retour_Materiel', 'materiel']


class Bon_Livraison_TitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bon_Livraison_Titan
        fields = ['commande', 'numero_BL',
                  'date_BL']
